# name

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A descriptive name for the reference object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * name;
```

## Discussion

For a reference object loaded from an Xcode asset catalog, this property is the name assigned in the asset catalog. You can also use this property to assign a name to an object you’ve recorded in an AR session using extractReferenceObject.

> **Note**:  This string is not localized text intended for user display. However, in debugging you can use this property to indicate which reference object was detected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/name)*