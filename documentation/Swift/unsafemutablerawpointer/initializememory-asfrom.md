# initializeMemory(as:from:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@discardableResult
func initializeMemory<C>(as type: C.Element.Type, from source: C) -> UnsafeMutablePointer<C.Element> where C : Collection
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/initializememory(as:from:))*