# Handling Errors with User-Driven Actions

**Framework**: File Provider

Handle any errors that occur while processing the action.

#### Overview

Whenever possible, handle the error in a way that allows the local action to succeed. If the local action can succeed, pass `nil` to the completion handler’s `error` property, and then fix any inconsistencies after the fact.

However, if an unrecoverable error occurs, do not make the local change. Instead, create an error object that describes the problem and pass it to the completion handler. In general, this error is presented to the user, and the action is canceled.

The following sections describe tactics for responding to specific error types.

##### Responding to Upload Errors

Handle any errors that occur while uploading the changes to your server  (such as [`NSFileProviderError.Code.insufficientQuota`](nsfileprovidererror/code/insufficientquota.md) errors)  by updating the item locally and setting its [`uploadingError`](nsfileprovideritemprotocol/uploadingerror.md) property. Upload errors should not prevent local changes. Instead, attempt to sync the change again, after the error is resolved.

For authentication errors, you can present a custom user interface using the [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) framework. For more information, see the [`FPUIActionExtensionViewController`](https://developer.apple.com/documentation/FileProviderUI/FPUIActionExtensionViewController) class’s [`prepare(forError:)`](https://developer.apple.com/documentation/FileProviderUI/FPUIActionExtensionViewController/prepare(forError:)) method.

##### Responding to Name Collisions

If a name collision occurs when syncing a local item with your server, update the local item, giving it a unique file name. A name collision is not considered an error.

If, however, you can detect a name collision locally, call the [`fileProviderErrorForCollision(with:)`](https://developer.apple.com/documentation/Foundation/NSError/fileProviderErrorForCollision(with:)) method to create a [`NSFileProviderError.Code.filenameCollision`](nsfileprovidererror/code/filenamecollision.md) error, and pass this error to the completion handler. The system then asks the user if they want to replace the existing item (taking into account its [`allowsTrashing`](nsfileprovideritemcapabilities/allowstrashing.md) and [`allowsDeleting`](nsfileprovideritemcapabilities/allowsdeleting.md) capabilities).

Perform all collision checks using case-insensitive comparisons, even if the filesystem or file provider allows case-sensitive names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/handling-errors-with-user-driven-actions)*