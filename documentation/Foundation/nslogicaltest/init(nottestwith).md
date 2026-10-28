# init(notTestWith:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(notTestWith subTest: NSScriptWhoseTest)
```

```objc
- (instancetype) initNotTestWithTest:(NSScriptWhoseTest *) subTest;
```

## Return Value

An `NSLogicalTest` object initialized to perform a `NOT` operation on `subTest`.

## Parameters

- `subTest`: The `NSScriptWhoseTest` object to invert.

## See Also

### Initializing a logical test
- [init(andTestWith: [NSSpecifierTest])](./init%28andtestwith%29.md)
  Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [init(orTestWith: [NSSpecifierTest])](./init%28ortestwith%29.md)
  Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogicaltest/init(nottestwith:))*