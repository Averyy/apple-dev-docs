# removeManagedReference(_:withOwner:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeManagedReference:(id) object withOwner:(id) owner;
```

#### Discussion

Use this method to deregister object relationships recorded using the [`addManagedReference(_:withOwner:)`](./addmanagedreference%28_,withowner%29.md) method.

The JavaScript garbage collector continues to scan any references that were reported to it until you use this method to remove those references.

## Parameters

- `object`: The object formerly referenced by the JavaScript memory management graph.
- `owner`: The other object responsible for the lifetime of the reference.

## See Also

### Managing Memory for Bridged Values
- [func addManagedReference(Any!, withOwner: Any!)](./addmanagedreference%28_,withowner%29.md)
  Notifies the JavaScriptCore virtual machine of an external object relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/removemanagedreference(_:withowner:))*