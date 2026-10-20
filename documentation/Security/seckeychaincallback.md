# SecKeychainCallback

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A customized callback function that keychain services call when a keychain event has occurred.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
typealias SecKeychainCallback = (SecKeychainEvent, UnsafeMutablePointer<SecKeychainCallbackInfo>, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef int (*)(enum SecKeychainEvent, struct SecKeychainCallbackInfo *, void *) SecKeychainCallback;
```

#### Return Value

A result code. See `Codes`.

#### Discussion

You would declare your keychain callback function like this if you were to name it `MyKeychainCallback`:

Listing 1. Declaring a keychain callback function

```objc
OSStatus MyKeychainCallback (
    SecKeychainEvent keychainEvent,
    SecKeychainCallbackInfo *info,
    void *context
);
```

To add your callback function, use the [`SecKeychainAddCallback(_:_:_:)`](./seckeychainaddcallback%28_,_,_%29.md) function. To remove your callback function, use the [`SecKeychainRemoveCallback(_:)`](./seckeychainremovecallback%28_%29.md) function.

## Parameters

- `keychainEvent`: The keychain event that occurred. The type of event that can trigger your callback depends on the bit mask you passed in the `eventMask` parameter of the function [`SecKeychainAddCallback(_:_:_:)`](./seckeychainaddcallback%28_,_,_%29.md). See [`SecKeychainEvent`](./seckeychainevent.md) for a list of possible values.
- `info`: A pointer to a structure of type [`SecKeychainCallbackInfo`](./seckeychaincallbackinfo.md). This structure provides your callback with information about the keychain event.
- `context`: A pointer to application-defined storage that your application previously passed to the function [`SecKeychainAddCallback(_:_:_:)`](./seckeychainaddcallback%28_,_,_%29.md). You can use this value to provide information that the callback function needs in order to properly handle the event, such as an object on which the callback function should call a method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincallback)*