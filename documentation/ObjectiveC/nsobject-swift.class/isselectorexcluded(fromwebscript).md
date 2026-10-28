# isSelectorExcluded(fromWebScript:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns whether a selector should be hidden from the scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func isSelectorExcluded(fromWebScript selector: Selector!) -> Bool
```

```objc
+ (BOOL) isSelectorExcludedFromWebScript:(SEL) selector;
```

## Return Value

[`YES`](../yes.md) if the selector specified by `aSelector` should be hidden from the scripting environment; otherwise, [`NO`](../no.md).

## Discussion

Only methods with valid parameters and return types are exported to the WebKit JavaScript environment. The valid types are Objective-C objects and scalars. The default value is [`YES`](../yes.md).

## Parameters

- `selector`: The selector.

## See Also

### Getting attributes
- [class func webScriptName(forKey: UnsafePointer<CChar>!) -> String!](./webscriptname%28forkey%29.md)
  Returns the scripting environment name for an attribute specified by a key.
- [class func webScriptName(for: Selector!) -> String!](./webscriptname%28for%29.md)
  Returns the scripting environment name for a selector.
- [class func isKeyExcluded(fromWebScript: UnsafePointer<CChar>!) -> Bool](./iskeyexcluded%28fromwebscript%29.md)
  Returns whether a key should be hidden from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isselectorexcluded(fromwebscript:))*