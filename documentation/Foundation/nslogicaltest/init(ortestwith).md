# init(orTestWith:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(orTestWith subTests: [NSSpecifierTest])
```

```objc
- (instancetype) initOrTestWithTests:(NSArray<NSSpecifierTest *> *) subTests;
```

## Return Value

An `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in `subTests`.

## Parameters

- `subTests`: An array of `NSSpecifierTest` objects representing Boolean expressions.

## See Also

### Initializing a logical test
- [init(andTestWith: [NSSpecifierTest])](./init%28andtestwith%29.md)
  Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [init(notTestWith: NSScriptWhoseTest)](./init%28nottestwith%29.md)
  Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogicaltest/init(ortestwith:))*