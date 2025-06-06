# readableTypeIdentifiersForItemProvider

**Framework**: Foundation  
**Kind**: property  
**Required**: Yes

An array of UTI strings representing the data types supported by the class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var readableTypeIdentifiersForItemProvider: [String] { get }
```

#### Discussion

Provide uniform type identifiers (UTIs) in order from highest fidelity to lowest. If your app employs a native data representation, place that first in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderreading/readabletypeidentifiersforitemprovider)*