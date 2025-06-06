# contactPrinter(_:)

**Framework**: UIKit  
**Kind**: method

Connects to the printer and gathers information about its capabilities.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contactPrinter() async -> Bool
```

#### Discussion

For printers you create yourself using the [`init(url:)`](uiprinter/init(url:).md) method, you must call this method prior to accessing properties containing printer-related information. This method runs asynchronously, returning immediately while the system continues to try and gather information about the printer’s name, location, capabilities, and so on. When the printer’s availability is determined, the results are delivered to the `completionHandler` block you provided.

Calling this method can take a significantly long time (up to 30 seconds), so after calling this method you should continue with other tasks. Use your completion handler block to update your app as appropriate.

## Parameters

- `completionHandler`: The block to execute with the results. This block has no return value and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/contactprinter(_:))*