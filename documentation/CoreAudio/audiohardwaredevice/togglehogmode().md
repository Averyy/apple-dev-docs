# toggleHogMode()

**Framework**: Core Audio  
**Kind**: method

Toggle exclusive access to the device for the current process. If another process owns exclusive access, that remains unchanged. If the current process owns exclusive access, it is released and made available to all processes again. If no process has exclusive access, this process gains ownership of exclusive access.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func toggleHogMode() throws -> pid_t
```

#### Return Value

A pid_t indicating the process that currently owns exclusive access to the device or a value of -1 indicating that the device is currently available to all processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/togglehogmode())*