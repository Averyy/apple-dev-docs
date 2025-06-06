# isKeyExcluded(fromWebScript:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns whether a key should be hidden from the scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func isKeyExcluded(fromWebScript name: UnsafePointer<CChar>!) -> Bool
```

#### Return Value

[`YES`](yes.md) if the attribute specified by `name` should be hidden from the scripting environment; otherwise, [`NO`](no.md).

#### Discussion

The default value is [`YES`](yes.md).

## Parameters

- `name`: The name of the attribute.

## See Also

- [class func webScriptName(forKey: UnsafePointer<CChar>!) -> String!](nsobject-swift.class/webscriptname(forkey:).md)
  Returns the scripting environment name for an attribute specified by a key.
- [class func webScriptName(for: Selector!) -> String!](nsobject-swift.class/webscriptname(for:).md)
  Returns the scripting environment name for a selector.
- [class func isSelectorExcluded(fromWebScript: Selector!) -> Bool](nsobject-swift.class/isselectorexcluded(fromwebscript:).md)
  Returns whether a selector should be hidden from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/iskeyexcluded(fromwebscript:))*