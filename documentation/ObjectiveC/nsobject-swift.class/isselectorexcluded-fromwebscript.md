# isSelectorExcluded(fromWebScript:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns whether a selector should be hidden from the scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func isSelectorExcluded(fromWebScript selector: Selector!) -> Bool
```

#### Return Value

[`YES`](yes.md) if the selector specified by `aSelector` should be hidden from the scripting environment; otherwise, [`NO`](no.md).

#### Discussion

Only methods with valid parameters and return types are exported to the WebKit JavaScript environment. The valid types are Objective-C objects and scalars. The default value is [`YES`](yes.md).

## Parameters

- `selector`: The selector.

## See Also

- [class func webScriptName(forKey: UnsafePointer<CChar>!) -> String!](nsobject-swift.class/webscriptname(forkey:).md)
  Returns the scripting environment name for an attribute specified by a key.
- [class func webScriptName(for: Selector!) -> String!](nsobject-swift.class/webscriptname(for:).md)
  Returns the scripting environment name for a selector.
- [class func isKeyExcluded(fromWebScript: UnsafePointer<CChar>!) -> Bool](nsobject-swift.class/iskeyexcluded(fromwebscript:).md)
  Returns whether a key should be hidden from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isselectorexcluded(fromwebscript:))*