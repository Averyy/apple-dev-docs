# init(andTestWith:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(andTestWith subTests: [NSSpecifierTest])
```

#### Return Value

An `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in `subTests`.

## Parameters

- `subTests`: An array of   objects representing Boolean expressions.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [init(notTestWith: NSScriptWhoseTest)](nslogicaltest/init(nottestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.
- [init(orTestWith: [NSSpecifierTest])](nslogicaltest/init(ortestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogicaltest/init(andtestwith:))*