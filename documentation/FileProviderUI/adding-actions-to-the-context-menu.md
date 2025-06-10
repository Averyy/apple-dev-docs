# Adding Actions to the Context Menu

**Framework**: File Provider UI

Present custom actions from your File Provider extension in the system’s file browser.

#### Overview

In your File Provider UI extension’s `Info.plist` file, you can define custom actions that appear in the context menu when the user long-presses an item while browsing your file provider’s content. When the user selects the action, the system presents a custom user interface element from your File Provider UI extension.

In macOS 11 and later, you can define custom actions directly in the File Provider extension. The system also adds these actions to the context menu; however, when the user selects them, your extension performs the action without presenting any additional UI elements. For more information, see [`NSFileProviderCustomAction`](https://developer.apple.com/documentation/FileProvider/NSFileProviderCustomAction).

##### Add Actions to the Context Menu

Add an `NSExtensionFileProviderActions` key to the `NSExtension` dictionary in your `Info.plist` file, as shown in the example below.

```xml
<key>NSExtensionFileProviderActions</key>
<array>
	<dict>
		<key>NSExtensionFileProviderActionIdentifier</key>
		<string>com.example.MyFileProvider.setRating</string>
		<key>NSExtensionFileProviderActionName</key>
		<string>Rate</string>
		<key>NSExtensionFileProviderActionActivationRule</key>
		<string>SUBQUERY( fileproviderItems, $fileproviderItem, $fileproviderItem.userInfo.rank != nil ).@count > 0</string>
	</dict>
</array>
```

The `NSExtensionFileProviderActions` key takes an array of dictionaries. Each dictionary represents a single action, and contains the keys shown in this table.

| Key | Type | Description |
| --- | --- | --- |
| `NSExtensionFileProviderActionIdentifier` | `String` | A unique identifier for the action. |
| `NSExtensionFileProviderActionName` | `String` (Localizable) | The localized name that appears in the context menu. |
| `NSExtensionFileProviderActionActivationRule` | `Predicate` | A predicate that determines whether the action appears in the context menu. |

The following sequence of events occurs when the user selects one of your actions from the context menu:

1. The system instantiates your [`FPUIActionExtensionViewController`](fpuiactionextensionviewcontroller.md) subclass.
2. The system calls your view controller’s [`prepare(forAction:itemIdentifiers:)`](fpuiactionextensionviewcontroller/prepare(foraction:itemidentifiers:).md) method. You can override this method to configure the user interface for the selected action.
3. The system presents your view controller to the user.
4. After the user has finished performing the action, you call the provided [`FPUIActionExtensionContext`](fpuiactionextensioncontext.md) object’s [`cancelRequest(withError:)`](fpuiactionextensioncontext/cancelrequest(witherror:).md) or [`completeRequest()`](fpuiactionextensioncontext/completerequest().md) method to complete the action.

##### Use Predicates to Enable and Disable Actions

Use the `NSExtensionFileProviderActionActivationRule` key to enable or disable actions based on the selected file provider item. Set the key’s value to a predicate format string that the system uses to create an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object. The system calls the predicate’s [`evaluate(with:)`](https://developer.apple.com/documentation/Foundation/NSPredicate/evaluate(with:)) method, passing in the selected item, a dictionary with a single `fileproviderItems` key. The value is an array of [`NSFileProviderItem`](https://developer.apple.com/documentation/FileProvider/NSFileProviderItem-swift.typealias) objects representing the selected items.

> ❗ **Important**: Your action must have a predicate or the system won’t display it in the action menu. To always show an action, use `TRUEPREDICATE`.

You can use predicates to test the value of any of the [`NSFileProviderItemProtocol`](https://developer.apple.com/documentation/FileProvider/NSFileProviderItemProtocol) object’s properties. For example, the following predicate tests whether the [`isUploaded`](https://developer.apple.com/documentation/FileProvider/NSFileProviderItemProtocol/isUploaded) property is set to [`true`](https://developer.apple.com/documentation/swift/true).

```other
SUBQUERY ( fileproviderItems, $fileproviderItem, $fileproviderItem.uploadded == YES ).@count > 0
```

You can also use predicates to test custom data that you’ve added to the item’s [`userInfo`](https://developer.apple.com/documentation/FileProvider/NSFileProviderItemProtocol/userInfo) dictionary. For example, the following predicate tests whether the `com.example.testBit` key has been set.

```other
SUBQUERY( fileproviderItems, $fileproviderItem, $fileproviderItem.userInfo."com.example.testBit" == YES ).@count > 0
```

If a predicate evaluates to [`true`](https://developer.apple.com/documentation/swift/true), the context menu includes the action; if [`false`](https://developer.apple.com/documentation/swift/false), the context menu doesn’t include the action. For more about creating predicate format strings, see [`Predicate Format String Syntax`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html#//apple_ref/doc/uid/TP40001795).

## See Also

- [class FPUIActionExtensionViewController](fpuiactionextensionviewcontroller.md)
  The custom user interface used to perform a selected action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/adding-actions-to-the-context-menu)*