# addManagedReference(_:withOwner:)

**Framework**: JavaScriptCore  
**Kind**: method

Notifies the JavaScriptCore virtual machine of an external object relationship.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addManagedReference(_ object: Any!, withOwner owner: Any!)
```

#### Discussion

Use this method to make the JavaScript runtime aware of arbitrary external Objective-C or Swift object graphs. The runtime can then use this information to retain any JavaScript values that are referenced from somewhere in said object graph.

For correct behavior, clients must make their external object graphs reachable from within the JavaScript runtime. If an Objective-C or Swift object is reachable from within the JavaScript runtime, all managed references transitively reachable from it as recorded using the [`addManagedReference(_:withOwner:)`](jsvirtualmachine/addmanagedreference(_:withowner:).md) method are scanned by the garbage collector.

## Parameters

- `object`: The object to be referenced by the JavaScript memory management graph.
- `owner`: The other object responsible for the lifetime of the reference.

## See Also

- [func removeManagedReference(Any!, withOwner: Any!)](jsvirtualmachine/removemanagedreference(_:withowner:).md)
  Notifies the JavaScriptCore virtual machine that a previously registered object relationship no longer exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/addmanagedreference(_:withowner:))*