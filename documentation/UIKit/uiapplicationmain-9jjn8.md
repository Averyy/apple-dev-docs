# UIApplicationMain(_:_:_:_:)

**Framework**: UIKit  
**Kind**: func

Creates the application object and the application delegate and sets up the event cycle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- Swift ?+

## Declaration

```swift
func UIApplicationMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, _ principalClassName: String?, _ delegateClassName: String?) -> Int32
```

#### Return Value

Even though an integer return type is specified, this function never returns. When users exits an iOS app by pressing the Home button, the application moves to the background.

#### Discussion

This function instantiates the application object from the principal class and instantiates the delegate (if any) from the given class and sets the delegate for the application. It also sets up the main event loop, including the application’s run loop, and begins processing events. If the application’s `Info.plist` file specifies a main nib file to be loaded, by including the [`NSMainNibFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMainNibFile) key and a valid nib file name for the value, this function loads that nib file.

Despite the declared return type, this function never returns.

## Parameters

- `argc`: The count of arguments in  ; this usually is the corresponding parameter to  .
- `argv`: A variable list of arguments; this usually is the corresponding parameter to  .
- `principalClassName`: The name of the   class or subclass. If you specify  ,   is assumed.
- `delegateClassName`: The name of the class from which the application delegate is instantiated. If   designates a subclass of  , you may designate the subclass as the delegate; the subclass instance receives the application-delegate messages. Specify   if you load the delegate object from your application’s main nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationmain(_:_:_:_:)-9jjn8)*