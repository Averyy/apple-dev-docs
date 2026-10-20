# shared

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The singleton app instance.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class var shared: UIApplication { get }
```

```objc
@property (class, nonatomic, readonly) UIApplication * sharedApplication;
```

#### Return Value

The app instance is created in the [`UIApplicationMain(_:_:_:_:)`](../uiapplicationmain%28_,_,_,_%29-1yub7.md) function.

#### Discussion

The [`UIApplicationMain(_:_:_:_:)`](../uiapplicationmain%28_,_,_,_%29-1yub7.md) function creates the shared app instance at launch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/shared)*