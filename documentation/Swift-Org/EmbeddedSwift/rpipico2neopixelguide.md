---
url: "https://docs.swift.org/latest/documentation/embeddedswift/rpipico2neopixelguide"
framework: "Swift-Org/EmbeddedSwift"
---

# Driving a NeoPixel LED on the Raspberry Pi Pico 2

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article  
**Download**: [rpi-pico2-neopixel](https://github.com/swiftlang/swift-embedded-examples/tree/main/rpi-pico2-neopixel)

Run a baremetal Swift program that drives a WS2812 NeoPixel RGB LED from an RP2350’s PIO block, with no SDK or operating system.

#### Overview

This example demonstrates how to program the RP2350’s PIO (Programmable I/O) peripheral directly from Swift MMIO register definitions, without depending on the Pico SDK. A small hand-assembled PIO program drives the WS2812 protocol’s timing-sensitive single-wire signal, and the CPU feeds pixel data into the PIO’s TX FIFO. The example targets a “SparkFun Pro Micro - RP2350” board, but works with other RP2350 boards.

The `configurePio` function loads the WS2812 PIO program and configures its clock divider and pin mapping, and `pioWritePixel` feeds a single pixel’s color into the state machine’s FIFO:

```swift
func pioWritePixel(_ hsv: HSV8Pixel) {
  let rgb = RGB8Pixel(hsv)

  // Pixels need to be G R B 0 left to right.
  let ws2812Value: UInt32 =
    UInt32(rgb.green) << 24 | UInt32(rgb.red) << 16 | UInt32(rgb.blue) << 8

  func txFifoFull() -> Bool {
    pio0.fstat.read().raw.txfull & 0x1 != 0
  }

  while txFifoFull() {}

  pio0.txf[0].write { w in
    w.raw.txf0 = ws2812Value
  }
}
```

> **Note**: This is a baremetal example — there’s no SDK or operating system involved. See [Using Embedded Swift in baremetal mode](./baremetal.md) for general guidance on baremetal Embedded Swift development.

#### Install Swift

Follow the instructions in [Installing Embedded Swift](./installembeddedswift.md) to install the latest Swift development snapshot with Embedded Swift support. Confirm the installation by running `swift --version` — it reports a “6.2-dev” or newer development snapshot.

#### Set the configuration

The example hardcodes the GPIO pin driving the NeoPixel in the `LED_PIN` constant in `Application.swift`. The “SparkFun Pro Micro - RP2350” needs no changes, but other boards need this constant adjusted to match their wiring:

```diff
-let LED_PIN: UInt32 = 25
+let LED_PIN: UInt32 = 18
```

#### Build the project

Navigate to the example directory and build it:

```shell
$ cd rpi-pico2-neopixel
$ make
```

#### Run on a device

Connect the Pico 2 board to your Mac using USB, and make sure it’s in USB Mass Storage firmware upload mode (hold the BOOTSEL button while plugging in the board, or make sure the flash memory doesn’t already contain valid firmware).

Copy the UF2 firmware to the mounted volume:

```shell
$ cp .build/armv7em-apple-none-macho/release/Application.uf2 /Volumes/RP2350
```

The RGB LED animates through the color wheel.

## See Also

### Raspberry Pi examples
- [Blinking an LED on the Raspberry Pi 4B](./rpi4bblinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 4B’s status LED, with no SDK or operating system.
- [Blinking an LED on the Raspberry Pi 5](./rpi5blinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 5’s status LED, with no SDK or operating system.
- [Blinking an LED in Morse code on the Raspberry Pi Pico W with the Pico SDK](./rpipicowblinkguide.md)
  Run a Swift program on a Raspberry Pi Pico W or Pico 2 W that signals “SOS” in Morse code using the Pico SDK’s Wi-Fi chip driver.
- [Blinking an LED in Morse code on the Raspberry Pi Pico](./rpipicoblinkguide.md)
  Run a baremetal Swift program on a Raspberry Pi Pico that spells “Hello Swift!” in Morse code on the onboard LED, with no SDK or operating system.
- [Building Harmony, a Bluetooth speaker and ferrofluid visualizer](./harmonyguide.md)
  Build and flash Harmony, a Raspberry Pi Pico W firmware in Swift that streams Bluetooth audio and drives a ferrofluid visualizer.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/rpipico2neopixelguide)*