# subscript(_:_:)

**Framework**: Create ML  
**Kind**: subscript  
**Role**: Instance Subscript

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript<T>(name: MLDataTable.Row.Key, type: T.Type) -> T? where T : MLDataValueConvertible { get }
```

## See Also

### Accessing rows
- [subscript(MLDataTable.Row.Key) -> MLDataTable.Row.Value?](./subscript%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/subscript(_:_:))*