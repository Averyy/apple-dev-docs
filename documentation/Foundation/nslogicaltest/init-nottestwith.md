# init(notTestWith:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(notTestWith subTest: NSScriptWhoseTest)
```

#### Return Value

An `NSLogicalTest` object initialized to perform a `NOT` operation on `subTest`.

## Parameters

- `subTest`: The   object to invert.

## See Also

- [init(andTestWith: [NSSpecifierTest])](nslogicaltest/init(andtestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [init(orTestWith: [NSSpecifierTest])](nslogicaltest/init(ortestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogicaltest/init(nottestwith:))*