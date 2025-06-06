# init(url:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a printer with the specified location.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(url: URL)
```

#### Return Value

A printer object representing the specified printer or `nil` if there was a problem initializing the object.

#### Discussion

Use this method to create printer objects for printers whose address you already know. The printer does not need to be online or available when you call this method. The URL you specify is stored in the returned object so that you can contact the printer later using the [`contactPrinter(_:)`](uiprinter/contactprinter(_:).md) method.

## Parameters

- `url`: A URL that identifies the location of the printer on your network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/init(url:))*