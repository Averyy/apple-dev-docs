# SecItemAdd(_:_:)

**Framework**: Security  
**Kind**: func

Adds one or more items to a keychain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecItemAdd(_ attributes: CFDictionary, _ result: UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus
```

## Mentions

- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)
- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)
- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)
- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

To add multiple items to a keychain at once use the [`kSecUseItemList`](ksecuseitemlist.md) key in the `attributes` dictionary with an array of dictionaries (each corresponding to one of the items) as its value. This is only supported for non-password items.

When you use Xcode to create an application, Xcode adds an `application-identifier` entitlement to the application bundle. Keychain Services uses this entitlement to grant the application access to its own keychain items. To share the new keychain item to among multiple apps, include the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) key in the `attributes` dictionary. The value of this key must be the name of a keychain access group to which all the programs that share this item belong.

##### Performance Considerations

`SecItemAdd` blocks the calling thread, so it can cause your app’s UI to hang if called from the main thread. Instead, call `SecItemAdd` from a background dispatch queue or `async` function:

**Swift**:

```swift
func addKeychainItem(attributes attrs: CFDictionary, _ completion: @escaping (OSStatus, CFTypeRef?) -> Void) {
    queue.async {
        var item: CFTypeRef?
        let result = SecItemAdd(attrs, &item)
        completion(result, item)
    }
}
```

**Objective-C**:

```objc
- (void)addKeychainItemWithAttributes:(CFDictionaryRef)attrs completion:(void(^)(OSStatus status, CFTypeRef item))completion {
    dispatch_async(backgroundQueue, ^{
        CFTypeRef item = NULL;
        OSStatus addResult = SecItemAdd(attrs, &item);
        completion(addResult, item);
        if (item) {
            CFRelease(item);
        }
    });
}
```

## Parameters

- `attributes`: A dictionary that describes the item to add. A typical `attributes` dictionary consists of: - **The item’s class.** Different attributes and behaviors apply to different classes of items. You use the [`kSecClass`](ksecclass.md) key with a suitable value to tell keychain services whether the data you want to store represents a password, a certificate, a cryptographic key, or something else. See [`Item class keys and values`](item-class-keys-and-values.md).
- **The data.** Use the [`kSecValueData`](ksecvaluedata.md) key to indicate the data you want to store. Keychain services takes care of encrypting this data if the item is secret, namely when it’s one of the password types or involves a private key.
- **Optional attributes.** Include attribute keys that help you find the item later, indicate how your app uses the data, and how the system shares the data. You can add any number of attributes, although many are specific to a particular class of item. For the attributes applicable to the keychain item you add, see the entry for the item’s class in [`Item class values`](item-class-keys-and-values#Item-class-values.md).
- **Optional return types.** Include return type keys to indicate what data, if any, you want returned upon successful completion. You often ignore the return data from a [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) call, in which case you don’t need to include any return result key. See [`Item return result keys`](item-return-result-keys.md) for more information.
- `result`: On return, a reference to the newly added items. The exact type of the result is based on the values supplied in `attributes`, as discussed in [`Item return result keys`](item-return-result-keys.md). Pass `nil` if you don’t need the result. Otherwise, your app becomes responsible for releasing the referenced object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemadd(_:_:))*