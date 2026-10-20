# resolveClassMethod(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Dynamically provides an implementation for a given selector for a class method.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func resolveClassMethod(_ sel: Selector!) -> Bool
```

```objc
+ (BOOL) resolveClassMethod:(SEL) sel;
```

#### Return Value

[`YES`](../yes.md) if the method was found and added to the receiver, otherwise [`NO`](../no.md).

#### Discussion

This method allows you to dynamically provide an implementation for a given selector. See [`resolveInstanceMethod(_:)`](./resolveinstancemethod%28_%29.md) for further discussion.

## Parameters

- `sel`: The name of a selector to resolve.

## See Also

### Dynamically Resolving Methods
- [class func resolveInstanceMethod(Selector!) -> Bool](./resolveinstancemethod%28_%29.md)
  Dynamically provides an implementation for a given selector for an instance method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/resolveclassmethod(_:))*