---
url: "https://docs.swift.org/latest/documentation/embeddedswift/stm32lcdlogoguide"
framework: "Swift-Org/EmbeddedSwift"
---

# Animating a Swift logo on the STM32F746G-DISCO’s LCD

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article  
**Download**: [stm32-lcd-logo](https://github.com/swiftlang/swift-embedded-examples/tree/main/stm32-lcd-logo)

Run a baremetal Swift program that drives the STM32F746G-DISCO’s onboard LCD panel, animating a bouncing Swift logo on a fading background.

#### Overview

This example demonstrates how to configure the STM32F7’s LTDC (LCD-TFT Display Controller) peripheral directly through Swift MMIO, without depending on an SDK. It sets up a background layer with a color that fades in and out, and a foreground layer containing pixel data for a Swift logo that bounces around the screen.

The `Application` entry point configures flash wait states and the LTDC clock, then loops forever, moving the logo layer and adjusting the background color:

```swift
import STM32F7X6
import Support

@main
struct Application {
  static func main() {
    configureFlash()
    initializeLTCD()
    ltdc.configure()

    var logoPosition = Point(x: 100, y: 100)
    var logoDelta = Point(x: 1, y: 1)

    while true {
      delay(milliseconds: 10)

      if logoPosition.x <= 0 || logoPosition.x >= maxLogoPosition.x {
        logoDelta.x *= -1
      }
      if logoPosition.y <= 0 || logoPosition.y >= maxLogoPosition.y {
        logoDelta.y *= -1
      }
      logoPosition = logoPosition.offset(by: logoDelta)
      ltdc.set(layer: 1, position: logoPosition)
    }
  }
}
```

> **Note**: This is a baremetal example — there’s no SDK or operating system involved. See [Using Embedded Swift in baremetal mode](./baremetal.md) for general guidance on baremetal Embedded Swift development. See [Blinking an LED on the STM32F746G-DISCO](./stm32blinkguide.md) for a simpler baremetal STM32F746G-DISCO example that only toggles a GPIO pin.

#### Install dependencies

Install the [stlink](https://github.com/stlink-org/stlink) command line tools, for example with `brew install stlink`.

#### Install Swift

Follow the instructions in [Installing Embedded Swift](./installembeddedswift.md) to install the latest Swift development snapshot with Embedded Swift support. Confirm the installation by running `swift --version` — it reports a “6.2-dev” or newer development snapshot.

#### Build the project

Navigate to the example directory and build it:

```shell
$ cd stm32-lcd-logo
$ make
```

#### Run on a device

Connect the STM32F746G-DISCO board to your Mac using the ST-LINK USB port. Flash the firmware:

```shell
$ st-flash --reset write .build/armv7em-apple-none-macho/release/Application.bin 0x08000000
```

The LCD display shows a bouncing, animated Swift logo on a fading background, and the user LED blinks.

#### Check the binary size

The compiled and linked binary is around 14 KB, split between roughly 3.5 KB of code and 10 KB of pixel data for the logo:

```console
$ size -m .build/armv7em-apple-none-macho/release/Application
Segment __TEXT: 14376
  Section __text: 3604
  Section __const: 10000
  total 13604
Segment __DATA: 8
  Section __nl_symbol_ptr: 4
  Section __data: 4
  total 8
Segment __VECTORS: 456
  Section __text: 456
  total 456
Segment __LINKEDIT: 1056
total 15896
```

## See Also

### STM32 examples
- [Blinking an LED on the STM32F746G-DISCO](./stm32blinkguide.md)
  Run a baremetal Swift MMIO program that blinks an LED on the STM32F746G-DISCO board, with no vendor SDKs or external toolchains.
- [Echoing UART input on the STM32F746G-DISCO](./stm32uartechoguide.md)
  Run a baremetal Swift program that echoes UART1 input on the STM32F746G-DISCO board, with no vendor SDKs or external toolchains.
- [Driving a NeoPixel LED strip on the STM32F746G-DISCO](./stm32neopixelguide.md)
  Run a baremetal Swift program that drives a NeoPixel WS2812 LED strip from the STM32F746G-DISCO board’s SPI peripheral, using DMA.
- [Running LVGL on the STM32F746G-DISCO](./stm32lvglguide.md)
  Run a full graphical Swift firmware on the STM32F746G-DISCO board, driving an LVGL user interface on the onboard LCD with touch input.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/stm32lcdlogoguide)*