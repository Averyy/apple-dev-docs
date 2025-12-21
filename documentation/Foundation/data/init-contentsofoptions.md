# init(contentsOf:options:)

**Framework**: Foundation  
**Kind**: init

Initialize a `Data` with the contents of a `URL`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(contentsOf url: URL, options: Data.ReadingOptions = []) throws
```

#### Discussion

> **Note**: An error in the Cocoa domain, if `url` cannot be read.

## Parameters

- `url`: The   to read.
- `options`: Options for the read operation. Default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(contentsof:options:))*