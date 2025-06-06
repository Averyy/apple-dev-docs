# init(orTestWith:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(orTestWith subTests: [NSSpecifierTest])
```

#### Return Value

An `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in `subTests`.

## Parameters

- `subTests`: An array of   objects representing Boolean expressions.

## See Also

- [init(andTestWith: [NSSpecifierTest])](nslogicaltest/init(andtestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [init(notTestWith: NSScriptWhoseTest)](nslogicaltest/init(nottestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogicaltest/init(ortestwith:))*