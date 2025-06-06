# initializeMemory(as:at:count:to:)

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
func initializeMemory<T>(as type: T.Type, at offset: Int = 0, count: Int = 1, to repeatedValue: T) -> UnsafeMutablePointer<T>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/initializememory(as:at:count:to:))*