# kJSClassAttributeNoAutomaticPrototype

**Framework**: JavaScriptCore  
**Kind**: var

An attribute that specifies that a class doesn’t automatically generate a shared prototype for its instance objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var kJSClassAttributeNoAutomaticPrototype: Int { get }
```

#### Discussion

Use [`kJSClassAttributeNoAutomaticPrototype`](kjsclassattributenoautomaticprototype.md) with [`JSObjectSetPrototype(_:_:_:)`](jsobjectsetprototype(_:_:_:).md) to manage prototypes manually.

## See Also

- [var kJSClassAttributeNone: Int](kjsclassattributenone.md)
  An attribute that specifies that a class has no special attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/kjsclassattributenoautomaticprototype)*