# resolveInstanceMethod(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Dynamically provides an implementation for a given selector for an instance method.

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
class func resolveInstanceMethod(_ sel: Selector!) -> Bool
```

#### Return Value

[`YES`](yes.md) if the method was found and added to the receiver, otherwise [`NO`](no.md).

#### Discussion

This method and [`resolveClassMethod(_:)`](nsobject-swift.class/resolveclassmethod(_:).md) allow you to dynamically provide an implementation for a given selector.

An Objective-C method is simply a C function that take at least two arguments—`self` and `_cmd`. Using the [`class_addMethod(_:_:_:_:)`](class_addmethod(_:_:_:_:).md) function, you can add a function to a class as a method. Given the following function:

```objc
void dynamicMethodIMP(id self, SEL _cmd)
{
    // implementation ....
}
```

you can use `resolveInstanceMethod:` to dynamically add it to a class as a method (called `resolveThisMethodDynamically`) like this:

```objc
+ (BOOL) resolveInstanceMethod:(SEL)aSEL
{
    if (aSEL == @selector(resolveThisMethodDynamically))
    {
          class_addMethod([self class], aSEL, (IMP) dynamicMethodIMP, "v@:");
          return YES;
    }
    return [super resolveInstanceMethod:aSel];
}
```

##### Special Considerations

This method is called before the Objective-C forwarding mechanism is invoked. If [`responds(to:)`](nsobjectprotocol/responds(to:).md) or [`instancesRespond(to:)`](nsobject-swift.class/instancesrespond(to:).md) is invoked, the dynamic method resolver is given the opportunity to provide an `IMP` for the given selector first.

## Parameters

- `sel`: The name of a selector to resolve.

## See Also

- [class func resolveClassMethod(Selector!) -> Bool](nsobject-swift.class/resolveclassmethod(_:).md)
  Dynamically provides an implementation for a given selector for a class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/resolveinstancemethod(_:))*