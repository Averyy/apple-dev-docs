# forKey(_:)

**Framework**: Foundation  
**Kind**: method

Returns the class description instance for the class type of the specified attribute or relationship.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func forKey(_ key: String) -> NSScriptClassDescription?
```

#### Return Value

The instance of `NSScriptClassDescription` for the type of the attribute or relationship specified by `key`. Returns `nil` if no scriptable property corresponds to `key`.

## Parameters

- `key`: The identifying key for an attribute or relationship of the receiver.

## See Also

- [init?(for: AnyClass)](nsscriptclassdescription/init(for:).md)
  Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.
- [var superclass: NSScriptClassDescription?](nsscriptclassdescription/superclass.md)
  Returns the class description instance for the superclass of the receiver’s class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/forkey(_:))*