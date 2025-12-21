# Configuring managed apps and extensions

**Framework**: Device Management

Provide managed apps and extensions with app configuration and secrets.

#### Overview

Device management services can configure managed apps and their extensions with declarative app configuration, which can consist of configuration data and secrets. With this feature, organizations can customize managed apps and extensions for their users. Managed apps and extensions use the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework to access declarative app configurations.

#### Configure a Managed App

The [`AppManaged`](appmanaged.md) configuration contains a `AppConfig` key that provides the declarative app configuration for managed apps. Secrets can be passwords, identities, or certificates. The `AppConfig` key specifies the declarative app configuration as a set of declarative management assets. This key is an object with the following keys:

| Key | Type | Description |
| --- | --- | --- |
| `DataAssetReference` | String | (Optional) The identifier of the asset declaration containing a reference to the configuration data |
| `Passwords` | Array | (Optional) An array of objects representing password data |
| `Identities` | Array | (Optional) An array of objects representing identity data |
| `Certificates` | Array | (Optional) An array of objects representing certificate data |

The device verifies the code signature of an app that requests declarative app configuration from the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework and ensures it matches the code signature of the installed managed app. The device provides declarative app configuration only to apps with verified code signatures.

##### Define the Asset to Provide Configuration Data

The `DataAssetReference` key in the [`AppManagedAppConfigDictionaryObject`](appmanagedappconfigdictionaryobject.md) object references an asset declaration that provides property list data. The asset declaration needs to be of type [`com.apple.asset.data`](https://developer.apple.com``/DeviceManagement/AssetData``) with its `ContentType` key set to the appropriate type. The asset data should be no larger than 1MB. The managed app’s developer specifies the data format within the property list.

##### Define the Assets to Provide Data for Secrets

The `Passwords`, `Identities`, and `Certificates` keys in the [`AppManagedAppConfigDictionaryObject`](appmanagedappconfigdictionaryobject.md) object are arrays of [`AppManagedCredentialConfigObject`](appmanagedcredentialconfigobject.md) objects, each containing the following keys:

| Key | Type | Description |
| --- | --- | --- |
| `Identifier` | String | (Required) The identifier the managed app uses to fetch the secret |
| `AssetReference` | String | (Required) The identifier of the asset declaration that contains a reference to the data for the secret |

The `Identifier` key contains a unique identifier for the secret that the managed app fetches using the APIs that the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework defines. The managed app’s developer specifies the allowed identifiers and how the app uses the secrets.

The `AssetReference` key references an asset declaration that provides the data for the secret. The parent object’s key determines the allowed asset types:

| Key | Allowed asset types |
| --- | --- |
| `Passwords` | [`com.apple.asset.credential.userpassword`](https://developer.apple.com``/DeviceManagement/AssetCredentialUserNameAndPassword``) |
| `Identities` | [`com.apple.asset.credential.identity`](https://developer.apple.com``/DeviceManagement/AssetCredentialIdentity``), [`com.apple.asset.credential.scep`](https://developer.apple.com``/DeviceManagement/AssetCredentialSCEP``), [`com.apple.asset.credential.acme`](https://developer.apple.com``/DeviceManagement/AssetCredentialACME``) |
| `Certificates` | [`com.apple.asset.credential.certificate`](https://developer.apple.com``/DeviceManagement/AssetCredentialCertificate``) |

#### Configure a Managed Apps Extensions

The device can also provide declarative app configuration for the managed app’s extensions. The `ExtensionConfigs` key specifies a dictionary whose keys are the composed identifiers of extensions, and whose values are objects that are the same as the [`AppManagedAppConfigDictionaryObject`](appmanagedappconfigdictionaryobject.md) object described above.

The extension’s composed identifier contains its bundle ID and team ID. To create it, start with the bundle ID, append a space, and then add the team ID in parentheses. For example, `com.example.app.extension (ABCDE12345)` is an extension with a bundle ID of `com.example.app.extension` and a team ID of `ABCDE12345`.

The device verifies the code signature of extensions that request declarative app configuration from the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework and matches it with the composed identifier. It provides declarative app configuration only to extensions with a verified code signature. For more information on code signing, see [`TN3127: Inside Code Signing: Requirements`](https://developer.apple.com/documentation/Technotes/tn3127-inside-code-signing-requirements).

#### Configure a Managed App with a Legacy App Configuration

For backward compatibility, the device supports configuring managed apps with legacy app configuration data to allow the apps to use the MDMv1 `UserDefaults`-based mechanism for reading configuration. This option allows device management services to configure a declarative managed app that uses legacy app configuration data, while waiting for the app developer to add support for the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework.

The [`AppManaged`](appmanaged.md) configuration’s `LegacyAppConfigAssetReference` key references an asset declaration for the legacy app configuration property list data. The corresponding asset needs to be of type [`com.apple.asset.data`](https://developer.apple.com``/DeviceManagement/AssetData``) with the asset’s `ContentType` key set to the appropriate type. The asset data should be no larger than 1 MB. The managed app’s developer specifies the data format within the property list.

Declarative management supports a many-to-many relationship between configurations and assets, so you can use the same asset for the legacy app configuration data and the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework-based app config data. This option allows a single set of configurations and assets to be compatible with older and newer versions of a managed app, where the older version supports only the legacy app configuration data capability, and the newer version uses the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework. The newer version of the managed app should support both the legacy app configuration data and the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework — the framework configuration takes precedence. This allows the developer to update the app without breaking MDM servers that haven’t transitioned to declarative app configuration yet.

## See Also

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)
  Use declarative management to handle all aspects of managing apps on devices.
- [Displaying managed apps and packages](displaying-managed-apps-and-packages.md)
  Use a management app to display managed apps and packages to the user.
- [Transferring management of apps to declarative management](transferring-management-of-apps-to-declarative-management.md)
  Seamlessly transition apps to declarative management without needing to reinstall.
- [Processing status for managed apps](processing-status-for-managed-apps.md)
  Process the status that declarative management reports for managed apps.
- [Installing packages](installing-packages.md)
  Use declarative package management to install and remove packages in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/configuring-managed-apps-and-extensions)*