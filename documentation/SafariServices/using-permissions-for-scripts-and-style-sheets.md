# Using permissions for scripts and style sheets

**Framework**: Safari Services

Learn about URL permissions for scripts and style sheets in a Safari app extension using information property list keys.

#### Overview

If you specify `Some` or `All` access for your Safari app extension, Safari can inject scripts or style sheets that your app extension provides into the webpage. In Safari 17 or later, users also need to grant your extension access to a website. For more information, see [`Adjusting website access permissions`](adjusting-website-access-permissions.md). By default, the setting is `All` access. However, you can set separate, precise controls for each file that define whether Safari injects it into the webpage.

For each file you add to the `SFSafariContentScript` and `SFSafariStyleSheet` sections of your app extension’s `Info.plist` file, you create a dictionary to describe the file. The required key specifies a path to the file. If you don’t specify any optional keys, Safari can inject the file into any website. You can add additional keys to this dictionary to permit or prevent injection of the file.

For both `SFSafariContentScript` and `SFSafariStyleSheet`, a key’s `Allowed URL Patterns` and `Excluded URL Patterns` subkeys work in conjunction with the `SFSafariWebsiteAccess` key to specify accessible webpages. First, the `SFSafariWebsiteAccess` values limit access, and then Safari applies the `Allowed URL Patterns` and `Excluded URL Patterns` keys. Here’s how these keys work:

- If you don’t specify either key, Safari can inject the file into any website.
- If you specify the `Allowed URL Patterns` key, Safari can inject the file only into webpages with a URL that matches one of these patterns. The value for this key is an array of domain patterns.
- If you specify the `Excluded URL Patterns` key, Safari can’t inject the file into any webpages with a URL that matches any of these patterns. The value for this key is an array of domain patterns.

These restrictions are in addition to those that you set in the `SFSafariWebsiteAccess` values. If you specify `Some` access for your app extension, you have access only to the domains matching your provided domain patterns. Items in `Allowed URL Patterns` and `Excluded URL Patterns` create additional restrictions within those domains. Be sure all the items in your `Allowed URL Patterns` are within a domain you have access to.

##### Specify Url Patterns

A URL pattern takes the form .

-  can be `http` or `https`.
-  is the host domain, such as `developer.apple.com` or `www.example.co.jp`.
-  is the directory or webpage, such as `safari/` or `safari/library/navigation/index.html`.

A URL pattern can include the asterisk (*) character to match any string. Using an asterisk, you can specify all pages in a particular domain without having to create an exhaustive list.

You can use the asterisk character anywhere in the domain or path, but not in the scheme. Here are some examples:

- `http://*/*`—Matches all HTTP URLs.
- `http://*.example.com/*`—Matches all webpages from `example.com`.
- `http://subdomain.example.com/*`—Matches all webpages from `subdomain.example.com`.
- `http://www.example.com/thepath/thepage.html`—Matches one webpage.
- `https://*/*`—Matches all webpages that Safari delivers over HTTPS.
- `https://secure.example.com/accounts/*`—Matches all webpages from the `accounts` directory of `secure.example.com` that Safari delivers over HTTPS.

> ❗ **Important**:  The format for URL patterns in `Allowed URL Patterns` and `Excluded URL Patterns` keys isn’t the same as the format for domain patterns in the `Allowed Domains` array that you specify in your website access list.  See [`Adjusting website access permissions`](adjusting-website-access-permissions.md).

 The format for URL patterns in `Allowed URL Patterns` and `Excluded URL Patterns` keys isn’t the same as the format for domain patterns in the `Allowed Domains` array that you specify in your website access list.  See [`Adjusting website access permissions`](adjusting-website-access-permissions.md).

## See Also

- [Setting Safari app extension feature keys](setting-safari-app-extension-feature-keys.md)
  Set keys for permissions, scripts, style sheets, contextual menu items, and toolbar items in the information property list file.
- [Adjusting website access permissions](adjusting-website-access-permissions.md)
  Set website access permissions in a Safari app extension using information property list keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/using-permissions-for-scripts-and-style-sheets)*