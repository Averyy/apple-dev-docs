# webScriptName(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the scripting environment name for an attribute specified by a key.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func webScriptName(forKey name: UnsafePointer<CChar>!) -> String!
```

#### Return Value

The name used to represent the attribute in the scripting environment.

## Parameters

- `name`: The name of the attribute.

## See Also

- [class func webScriptName(for: Selector!) -> String!](nsobject-swift.class/webscriptname(for:).md)
  Returns the scripting environment name for a selector.
- [class func isSelectorExcluded(fromWebScript: Selector!) -> Bool](nsobject-swift.class/isselectorexcluded(fromwebscript:).md)
  Returns whether a selector should be hidden from the scripting environment.
- [class func isKeyExcluded(fromWebScript: UnsafePointer<CChar>!) -> Bool](nsobject-swift.class/iskeyexcluded(fromwebscript:).md)
  Returns whether a key should be hidden from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webscriptname(forkey:))*