---
url: "https://docs.swift.org/latest/documentation/embeddedswift/examples"
framework: "Swift-Org/EmbeddedSwift"
---

# Examples

**Framework**: Swift-Org/EmbeddedSwift

Explore complete, step-by-step projects for popular embedded platforms.

#### Overview

These examples walk through complete projects for popular embedded boards, covering everything from basic LED blinking to UART communication, NeoPixel control, and display output. Each example includes the full Swift source code and build instructions, and includes wiring diagrams or schematics where applicable.

## Topics

### Essentials
- [Trying out Embedded Swift on macOS](./macosguide.md)
  Build a simple program for your host OS with Embedded Swift.
- [Debugging with SVD2LLDB](./svd2lldbguide.md)
  Debug Swift Embedded code on Raspberry Pi Pico boards using LLDB hardware debugging features.
- [Blinking an LED on the Raspberry Pi Pico with the Pico SDK](./rpipicoguide.md)
  Target a Raspberry Pi Pico as an embedded device that runs a simple Swift program.
- [Setting up a baremetal STM32 project with Embedded Swift](./stm32baremetalguide.md)
  Program a STM32 microcontroller directly with low-level Swift code.
### STM32 examples
- [Blinking an LED on the STM32F746G-DISCO](./stm32blinkguide.md)
  Run a baremetal Swift MMIO program that blinks an LED on the STM32F746G-DISCO board, with no vendor SDKs or external toolchains.
- [Echoing UART input on the STM32F746G-DISCO](./stm32uartechoguide.md)
  Run a baremetal Swift program that echoes UART1 input on the STM32F746G-DISCO board, with no vendor SDKs or external toolchains.
- [Driving a NeoPixel LED strip on the STM32F746G-DISCO](./stm32neopixelguide.md)
  Run a baremetal Swift program that drives a NeoPixel WS2812 LED strip from the STM32F746G-DISCO board’s SPI peripheral, using DMA.
- [Animating a Swift logo on the STM32F746G-DISCO’s LCD](./stm32lcdlogoguide.md)
  Run a baremetal Swift program that drives the STM32F746G-DISCO’s onboard LCD panel, animating a bouncing Swift logo on a fading background.
- [Running LVGL on the STM32F746G-DISCO](./stm32lvglguide.md)
  Run a full graphical Swift firmware on the STM32F746G-DISCO board, driving an LVGL user interface on the onboard LCD with touch input.
### ESP32 examples
- [Blinking an LED on the ESP32](./esp32guide.md)
  Run a Swift LED-blink program on a RISC-V ESP32 device using the ESP-IDF SDK.
- [Echoing UART input on the ESP32](./esp32uartechoguide.md)
  Run a Swift UART echo program on a RISC-V ESP32 device using the ESP-IDF SDK.
- [Driving a WS2812 LED strip on the ESP32](./esp32ledstripguide.md)
  Run a Swift program that animates a WS2812 LED strip on a RISC-V ESP32 device using the ESP-IDF SDK.
### Raspberry Pi examples
- [Blinking an LED on the Raspberry Pi 4B](./rpi4bblinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 4B’s status LED, with no SDK or operating system.
- [Blinking an LED on the Raspberry Pi 5](./rpi5blinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 5’s status LED, with no SDK or operating system.
- [Blinking an LED in Morse code on the Raspberry Pi Pico W with the Pico SDK](./rpipicowblinkguide.md)
  Run a Swift program on a Raspberry Pi Pico W or Pico 2 W that signals “SOS” in Morse code using the Pico SDK’s Wi-Fi chip driver.
- [Blinking an LED in Morse code on the Raspberry Pi Pico](./rpipicoblinkguide.md)
  Run a baremetal Swift program on a Raspberry Pi Pico that spells “Hello Swift!” in Morse code on the onboard LED, with no SDK or operating system.
- [Driving a NeoPixel LED on the Raspberry Pi Pico 2](./rpipico2neopixelguide.md)
  Run a baremetal Swift program that drives a WS2812 NeoPixel RGB LED from an RP2350’s PIO block, with no SDK or operating system.
- [Building Harmony, a Bluetooth speaker and ferrofluid visualizer](./harmonyguide.md)
  Build and flash Harmony, a Raspberry Pi Pico W firmware in Swift that streams Bluetooth audio and drives a ferrofluid visualizer.
### Other platform examples
- [Blinking an LED on Nordic nRF with Zephyr](./nrfblinkguide.md)
  Run a Swift LED-blink program on an Arm Cortex-M nRF board using the Zephyr RTOS SDK.
- [Blinking LEDs on NuttX RTOS with QEMU](./nuttxriscvblinkguide.md)
  Run a Swift LED-blink program on Apache NuttX RTOS, emulated on a RISC-V QEMU target.

## See Also

### Installation and usage
- [Installing Embedded Swift](./installembeddedswift.md)
  Get the tools needed to use Embedded Swift.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/examples)*