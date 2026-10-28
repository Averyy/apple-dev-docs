---
url: "https://docs.swift.org/latest/documentation/embeddedswift/stm32lvglguide"
framework: "Swift-Org/EmbeddedSwift"
---

# Running LVGL on the STM32F746G-DISCO

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article  
**Download**: [stm32-lvgl](https://github.com/swiftlang/swift-embedded-examples/tree/main/stm32-lvgl)

Run a full graphical Swift firmware on the STM32F746G-DISCO board, driving an LVGL user interface on the onboard LCD with touch input.

## Overview

This example demonstrates a complete baremetal graphical application: it links an ELF binary using `lld` and a custom linker script instead of the Mach-O toolchain the other STM32 examples use, so it builds identically on macOS and Linux hosts. It uses the LLVM Embedded Toolchain for Arm, the LVGL graphics library for UI rendering, and configures the STM32F746G’s DRAM, LCD, touch panel, GPIO pins, and interrupts entirely from Swift and C startup code, with no other SDK or library dependencies.

![An LVGL user interface running on the STM32F746G-DISCO’s LCD.](https://docs.swift.org/latest/images/EmbeddedSwift/STM32LvglGuide-hero.gif)

The same “business logic” code that drives the LVGL UI on the board also runs in a host OS “simulator” that renders the UI through SDL, so UI code can be developed and iterated on without hardware.

> **Note**: This is a baremetal example — there’s no SDK or operating system involved. See [Using Embedded Swift in baremetal mode](./baremetal.md) for general guidance on baremetal Embedded Swift development. See [Blinking an LED on the STM32F746G-DISCO](./stm32blinkguide.md) for a much simpler baremetal STM32F746G-DISCO example that only toggles a GPIO pin.

## Install dependencies

Install the [stlink](https://github.com/stlink-org/stlink) command line tools, for example with `brew install stlink`.

## Install Swift

Install the Swift toolchain version specified in this repository’s `.swift-version` file. The recommended way to do this is with [swiftly](https://www.swift.org/swiftly/):

```shell
$ cd stm32-lvgl
$ swiftly install
```

Fetch the LVGL and LLVM Embedded Toolchain for Arm dependencies with the provided script:

```shell
$ ./fetch-dependencies.sh
```

## Build the project

Build the firmware:

```shell
$ make
```

## Run on a device

Connect the STM32F746G-DISCO board to your Mac using the ST-LINK USB port. Flash the firmware:

```shell
$ make flash
```

The UI animates on the board’s LCD display, and the touch screen reacts to input.

## Run in the simulator

Build and run the same UI code in a desktop SDL simulator, without hardware:

```shell
$ make simulator
```

## Learn more about the linker script

The ELF linking, linker script, and packaging scheme are described in detail inside the [linker script](https://github.com/swiftlang/swift-embedded-examples/blob/main/stm32-lvgl/Sources/Support/linkerscript.ld).

## See Also

### STM32 examples
- [Blinking an LED on the STM32F746G-DISCO](./stm32blinkguide.md)
  Run a baremetal Swift MMIO program that blinks an LED on the STM32F746G-DISCO board, with no vendor SDKs or external toolchains.
- [Echoing UART input on the STM32F746G-DISCO](./stm32uartechoguide.md)
  Run a baremetal Swift program that echoes UART1 input on the STM32F746G-DISCO board, with no vendor SDKs or external toolchains.
- [Driving a NeoPixel LED strip on the STM32F746G-DISCO](./stm32neopixelguide.md)
  Run a baremetal Swift program that drives a NeoPixel WS2812 LED strip from the STM32F746G-DISCO board’s SPI peripheral, using DMA.
- [Animating a Swift logo on the STM32F746G-DISCO’s LCD](./stm32lcdlogoguide.md)
  Run a baremetal Swift program that drives the STM32F746G-DISCO’s onboard LCD panel, animating a bouncing Swift logo on a fading background.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/stm32lvglguide)*