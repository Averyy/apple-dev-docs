# contact

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The associated contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var contact: CNContact { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) CNContact * contact;
```

*macOS*

```objc
@property (atomic, copy, readonly) CNContact * contact;
```

## Discussion

This property is used for properties that may or may not be in labeled arrays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty/contact)*