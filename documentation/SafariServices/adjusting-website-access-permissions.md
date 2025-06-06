# Adjusting website access permissions

**Framework**: Safari Services

Set website access permissions in a Safari app extension using information property list keys.

#### Overview

In Safari 16 and earlier, set permissions for the webpages and domains your app extension accesses in the `Info.plist` file. In Safari 17 and later, users also grant and manage access to webpages and domains that your app extension specifies in the `Info.plist` file.

##### Setting Permissions

Set the webpages and domains your app extension has access to using the `Info.plist` file. Adding the `SFSafariWebsiteAccess` dictionary to the `NSExtension` element in the file specifies the webpages your app extension has access to. The system only injects your app extension’s content into the webpages you specify, and your app extension can only manipulate the webpages you specify with the [`SFSafariPageProperties`](sfsafaripageproperties.md) object in your app extension. For website access, specify the available subkeys.

| Subkey | Type | Description |
| --- | --- | --- |
| `Level` | String | A string that specifies the extent of the app extension’s website access. Available values are `All`, `None`, `Some`. |
| `Allowed Domains` | Array | Use this subkey only if `Level` is `Some`. The `Allowed Domains` subkey lists the allowed domains. Each domain in the array is specified as a string. |

Use the `Level` subkey to restrict your extension’s website access. Available values are:

- `None`—Your app extension can’t access any webpage by injecting scripts or style sheets, and most page properties are undefined.
- `All`—Your app extension has access to all webpages and domains.
- `Some`—Your app extension can access webpages from a list of domains.

If you specify the value `Some`, you must also add the `Allowed Domains` key to the dictionary. The value for this key is an array specifying the domains that the app extension can access.

If you set your access to `Some`, and you don’t specify any domain patterns, your app extension can’t access any webpages.

Each domain is specified as a string, such as `developer.apple.com` or `www.example.org.jp`. Don’t include a scheme, such as `http://,` in the domain pattern.

A leading asterisk (*) character matches all subdomains of the allowed domain. For example, `*.apple.com` matches `www.apple.com`, `developer.apple.com`, or any host name in the `apple.com` domain. Similarly, `*.co.jp` matches all `co.jp` domains, and `*.jp` matches all `.jp` domains.

##### Grant and Manage Permissions

In Safari 17 and later, the first time the user visits a page where they haven’t granted access to your Safari app extension, Safari shows a badge next to your toolbar button that indicates the user needs to interact with the extension to grant it permission. The user clicks the toolbar button and selects an option to grant permission: for 24 hours on this website, always for this website, or always for all websites.

The user may then manage permissions for your extension. Choose Safari > Settings and click the Extensions tab to see a summary of permission statuses for each extension. Then they can click the Websites tab and select the extension to see which websites have been configured for it. They can also change the permission status for a selected website to Ask, Allow, or Deny.

When you grant access to an extension for a specific web site, that grants the extension access to the site across all profiles, private browsing, and browsing without a profile.

## See Also

- [Setting Safari app extension feature keys](setting-safari-app-extension-feature-keys.md)
  Set keys for permissions, scripts, style sheets, contextual menu items, and toolbar items in the information property list file.
- [Using permissions for scripts and style sheets](using-permissions-for-scripts-and-style-sheets.md)
  Learn about URL permissions for scripts and style sheets in a Safari app extension using information property list keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/adjusting-website-access-permissions)*