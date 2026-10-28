# objectAtIndexedSubscript(_:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Returns the value’s JavaScript property at the specified index, allowing subscript syntax.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func objectAtIndexedSubscript(_ index: Int) -> JSValue!
```

```objc
- (JSValue *) objectAtIndexedSubscript:(NSUInteger) index;
```

## Return Value

The value at the specified index, or the JavaScript `undefined` value if no property exists at that index.

## Discussion

This method is equivalent to the [`atIndex(_:)`](./atindex%28_%29.md) method, but provides Objective-C subscripting support.

## Parameters

- `index`: An index in the JavaScript object.

## See Also

### Accessing Values with Subscript Syntax
- [func setObject(Any!, atIndexedSubscript: Int)](./setobject%28_,atindexedsubscript%29.md)
  Sets the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func objectForKeyedSubscript(Any!) -> JSValue!](./objectforkeyedsubscript%28_%29.md)
  Returns the value’s JavaScript property named with the specified key, allowing subscript syntax.
- [func setObject(Any!, forKeyedSubscript: Any!)](./setobject%28_,forkeyedsubscript%29.md)
  Sets the value’s JavaScript property named with the specified key, allowing subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/objectatindexedsubscript(_:))*