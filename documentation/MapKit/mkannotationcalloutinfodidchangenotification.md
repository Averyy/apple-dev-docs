# MKAnnotationCalloutInfoDidChangeNotification

**Framework**: MapKit  
**Kind**: var  
**Role**: Global Variable

A property to observe to determine when the title or subtitle information of an annotation object changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

> **Deprecated**: Use KVO notifications instead.

## Declaration

```c
extern NSString * const MKAnnotationCalloutInfoDidChangeNotification;
```

#### Discussion

This notification supports legacy applications and is no longer necessary. MapKit tracks changes to the title and subtitle of an annotation using KVO notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationcalloutinfodidchangenotification)*