# Processing status for managed apps

**Framework**: Device Management

Process the status that declarative management reports for managed apps.

#### Overview

Devices report the status of each declarative managed app in the [`StatusAppManagedList`](statusappmanagedlist.md) status item, which device management servers can subscribe to. Devices report incremental updates to the [`StatusAppManagedList`](statusappmanagedlist.md) status item elements when the managed app status changes.

#### Process the Status Item

The [`StatusAppManagedList`](statusappmanagedlist.md) status item type is `app.managed.list`, which contains the device’s declarative managed apps.

The status item value is an array of objects that represent each managed app. The device reports changes incrementally to the device management server using normal status-item array value reporting behavior (see [`StatusReport`](statusreport.md)). The status includes required and optional apps, whether installed or not.

The `identifier` key is the bundle ID of the managed app and is the unique identifier for incremental reporting of the overall status item (see [`StatusReport`](statusreport.md)). The `declaration-identifier` key is the `Identifier` of the managed app configuration. Additional properties show the app’s name and version identifiers.

The `state` key indicates the app’s management state, for example, `queued`, `downloading`, `installing`, and `managed`. If an error occurs, the device reports the `failed` state with the `reasons` key for more details. The device can also include the `reasons` key for other states, providing additional information, for example, if an update for the app is available.

If a configuration provisions declarative app configurations for an app or its extensions, the app or extension reports the state back to the device management server using the `config-state` key. The device management service should communicate errors back to the admin for corrective actions.

#### Use Managed App Status in a Predicate

You can include managed app status in declarative device management activation predicates to test the status values and trigger activations based on them. To use properties of a specific app in a predicate term, use the `SUBQUERY` operator. The following example shows a predicate that triggers when an app’s management state is set to `managed`:

```None
SUBQUERY(@status(app.managed.list), $app, ($app.@key(identifier) == "com.example.app") AND ($app.@key(state) == "managed")).@count != 0
```

The first argument of the `SUBQUERY` specifies the `app.managed.list` status item array value. The second argument defines an internal variable, `$app`, that refers to each item in the array. The third term is a predicate expression that applies to each item in the array; if an item matches, it’s included in the array that is the result of the `SUBQUERY`. This expression uses the `$app` variable to reference the item in the `app.managed.list` it operates on.

In this example, two terms exist: one tests for a specific app bundle identifier, and the other tests the app’s state. The `@count != 0` term tests whether the `SUBQUERY` result array contains at least one matching item. So this predicate evaluates to `true` only if the app with the bundle identifier `com.example.app` is present and its management state is set to `managed`. To learn more about predicate expressions, see [`Predicate Programming`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html).

## See Also

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)
  Use declarative management to handle all aspects of managing apps on devices.
- [Displaying managed apps and packages](displaying-managed-apps-and-packages.md)
  Use a management app to display managed apps and packages to the user.
- [Configuring managed apps and extensions](configuring-managed-apps-and-extensions.md)
  Provide managed apps and extensions with app configuration and secrets.
- [Transferring management of apps to declarative management](transferring-management-of-apps-to-declarative-management.md)
  Seamlessly transition apps to declarative management without needing to reinstall.
- [Installing packages](installing-packages.md)
  Use declarative package management to install and remove packages in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/processing-status-for-managed-apps)*