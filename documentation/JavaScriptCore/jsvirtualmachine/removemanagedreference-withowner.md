# removeManagedReference(_:withOwner:)

**Framework**: JavaScriptCore  
**Kind**: method

Notifies the JavaScriptCore virtual machine that a previously registered object relationship no longer exists.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeManagedReference(_ object: Any!, withOwner owner: Any!)
```

#### Discussion

Use this method to deregister object relationships recorded using the [`addManagedReference(_:withOwner:)`](jsvirtualmachine/addmanagedreference(_:withowner:).md) method.

The JavaScript garbage collector continues to scan any references that were reported to it until you use this method to remove those references.

## Parameters

- `object`: The object formerly referenced by the JavaScript memory management graph.
- `owner`: The other object responsible for the lifetime of the reference.

## See Also

- [func addManagedReference(Any!, withOwner: Any!)](jsvirtualmachine/addmanagedreference(_:withowner:).md)
  Notifies the JavaScriptCore virtual machine of an external object relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/removemanagedreference(_:withowner:))*