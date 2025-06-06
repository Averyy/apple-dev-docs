# base

**Framework**: Swift  
**Kind**: property

The value wrapped by this instance.

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
var base: Any { get }
```

#### Discussion

The `base` property can be cast back to its original type using one of the type casting operators (`as?`, `as!`, or `as`).

```swift
let anyMessage = AnyHashable("Hello world!")
if let unwrappedMessage = anyMessage.base as? String {
    print(unwrappedMessage)
}
// Prints "Hello world!"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyhashable/base)*