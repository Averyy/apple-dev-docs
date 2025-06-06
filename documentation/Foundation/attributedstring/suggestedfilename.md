# suggestedFilename

**Framework**: Foundation  
**Kind**: property

A suggested filename of a `Transferable` value.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
var suggestedFilename: String? { get }
```

#### Discussion

A filename for given item, or `nil` if none specified. A name can be specified using `TransferRepresentation.suggestedFileName(_:)`. The default implementation of this property is available to all types that conform to `Transferable` protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/suggestedfilename)*