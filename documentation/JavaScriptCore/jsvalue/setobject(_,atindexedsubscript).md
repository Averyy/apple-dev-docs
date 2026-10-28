# setObject(_:atIndexedSubscript:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Sets the value’s JavaScript property at the specified index, allowing subscript syntax.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setObject(_ object: Any!, atIndexedSubscript index: Int)
```

```objc
- (void) setObject:(id) object atIndexedSubscript:(NSUInteger) index;
```

## Discussion

This method is equivalent to the [`setValue(_:at:)`](./setvalue%28_,at%29.md) method, but provides Objective-C subscripting support.

## Parameters

- `object`: The value to set at the specified index.
- `index`: An index in the JavaScript object.

## See Also

### Accessing Values with Subscript Syntax
- [func objectAtIndexedSubscript(Int) -> JSValue!](./objectatindexedsubscript%28_%29.md)
  Returns the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func objectForKeyedSubscript(Any!) -> JSValue!](./objectforkeyedsubscript%28_%29.md)
  Returns the value’s JavaScript property named with the specified key, allowing subscript syntax.
- [func setObject(Any!, forKeyedSubscript: Any!)](./setobject%28_,forkeyedsubscript%29.md)
  Sets the value’s JavaScript property named with the specified key, allowing subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/setobject(_:atindexedsubscript:))*