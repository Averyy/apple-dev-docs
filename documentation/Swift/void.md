# Void

**Framework**: Swift  
**Kind**: typealias

The return type of functions that don’t explicitly specify a return type, that is, an empty tuple `()`.

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
typealias Void = ()
```

#### Discussion

When declaring a function or method, you don’t need to specify a return type if no value will be returned. However, the type of a function, method, or closure always includes a return type, which is `Void` if otherwise unspecified.

Use `Void` or an empty tuple as the return type when declaring a closure, function, or method that doesn’t return a value.

```swift
// No return type declared:
func logMessage(_ s: String) {
    print("Message: \(s)")
}

let logger: (String) -> Void = logMessage
logger("This is a void function")
// Prints "Message: This is a void function"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/void)*