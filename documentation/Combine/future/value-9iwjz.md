# value

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

The published value of the future, delivered asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
final var value: Output { get async }
```

Available when `Failure` is `Never`.

#### Discussion

This property subscribes to the `Future` and delivers the value asynchronously when the `Future` publishes it. Use this property when you want to use the `async`-`await` syntax with a `Future`.

## See Also

### Accessing the value asynchronously
- [var value: Output](./value-5iprp.md)
  The published value of the future or an error, delivered asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/future/value-9iwjz)*