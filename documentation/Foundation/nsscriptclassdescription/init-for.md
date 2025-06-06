# init(for:)

**Framework**: Foundation  
**Kind**: init

Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(for aClass: AnyClass)
```

#### Return Value

The class description for the class specified by `aClass` or, if that class isn’t scriptable, for the class description for the first superclass that is. Returns `nil` if it doesn’t find a scriptable class.

## Parameters

- `aClass`: The class whose description is needed.

## See Also

- [func forKey(String) -> NSScriptClassDescription?](nsscriptclassdescription/forkey(_:).md)
  Returns the class description instance for the class type of the specified attribute or relationship.
- [var superclass: NSScriptClassDescription?](nsscriptclassdescription/superclass.md)
  Returns the class description instance for the superclass of the receiver’s class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/init(for:))*