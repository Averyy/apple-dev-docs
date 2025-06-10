# body

**Framework**: Swift  
**Kind**: property

A builder expression that describes the process of importing and exporting an item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var body: Never { get }
```

#### Discussion

Combine multiple existing transfer representations to compose a single transfer representation that describes how to transfer an item in multiple scenarios.

```swift
struct CombinedRepresentation: TransferRepresentation {
   var body: some TransferRepresentation {
       DataRepresentation(...)
       FileRepresentation(...)
   }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/body-swift.property)*