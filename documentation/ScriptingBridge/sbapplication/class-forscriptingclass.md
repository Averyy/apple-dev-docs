# class(forScriptingClass:)

**Framework**: Scripting Bridge  
**Kind**: method

Returns a class object that represents a particular class in the target application.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func `class`(forScriptingClass className: String) -> AnyClass?
```

#### Return Value

A `Class` object representing the scripting class.

#### Discussion

You invoke this method on an instance of a scriptable application. Once you have the class object, you may allocate an instance of the class and appropriately the raw instance. Or you may use it in a call to [`isKind(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isKind(of:)) to determine the class type of an object.

## Parameters

- `className`: The name of the scripting class, as it appears in the scripting interface. For example, “document”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/class(forscriptingclass:))*