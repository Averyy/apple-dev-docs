# webScriptName(for:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the scripting environment name for a selector.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func webScriptName(for selector: Selector!) -> String!
```

#### Return Value

The name used to represent the selector in the scripting environment.

#### Discussion

It is your responsibility to ensure that the returned name is unique to the script invoking this method. If this method returns `nil` or you do not implement it, the default name for the selector is constructed as follows:

- A colon (”:”) in the Objective-C selector is replaced by an underscore (”_”).
- An underscore in the Objective-C selector is prefixed with a dollar sign (”$”).
- A dollar sign in the Objective-C selector is prefixed with another dollar sign.

The following table shows examples of how the default name is constructed:

| Objective-C selector | Default script name for selector |
| --- | --- |
| `setFlag:` | `setFlag_` |
| `setFlag:forKey:withAttributes:` | `setFlag_forKey_withAttributes_` |
| `propertiesForExample_Object:` | `propertiesForExample$_Object_` |
| `set_$_forKey:withDictionary:` | `set$_$$_$_forKey_withDictionary_` |

Since the default construction for a method name can be confusing depending on its Objective-C name, you should implement this method and return a more human-readable name.

## Parameters

- `selector`: The selector.

## See Also

- [class func webScriptName(forKey: UnsafePointer<CChar>!) -> String!](nsobject-swift.class/webscriptname(forkey:).md)
  Returns the scripting environment name for an attribute specified by a key.
- [class func isSelectorExcluded(fromWebScript: Selector!) -> Bool](nsobject-swift.class/isselectorexcluded(fromwebscript:).md)
  Returns whether a selector should be hidden from the scripting environment.
- [class func isKeyExcluded(fromWebScript: UnsafePointer<CChar>!) -> Bool](nsobject-swift.class/iskeyexcluded(fromwebscript:).md)
  Returns whether a key should be hidden from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webscriptname(for:))*