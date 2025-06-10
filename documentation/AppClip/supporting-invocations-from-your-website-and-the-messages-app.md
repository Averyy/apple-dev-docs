# Supporting invocations from your website and the Messages app

**Framework**: App Clips

Display a Smart App Banner and the App Clip card on your website that people tap to launch your App Clip, and add support for invocations from the Messages app.

#### Overview

When you create your App Clip, register a . By creating a default App Clip experience, you lay the foundation for supporting  from a Smart App Banner on your website. This has an added benefit: If a person shares a link to your website in the Messages app and the website displays a Smart App Banner, the recipient can tap the link to instantly launch your App Clip.

Additionally, you can display the App Clip card on your website if a person’s device runs iOS 15 or later. This makes your App Clip even more discoverable and reduces the number of taps required to launch your App Clip.

![Two screenshots of a website in Safari on iPhone. One screenshot shows the Smart App Banner on the website. The other screenshot shows the App Clip card in Safari.](https://docs-assets.developer.apple.com/published/4984d42c98963fb04ce57a2fa0b2529c/media-3886822%402x.png)

Note that the Smart App Banner only appears on your website if:

- You associated your App Clip with the website where you want to display the banner.
- You added the banner to your website’s source code.
- You configured the default App Clip experience.
- You published a version of your app that offers an App Clip.
- A person opens the website in an [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) or in Safari without Private Browsing enabled.

With the App Clip card on your website, people don’t need to tap the Smart App Banner for the card to appear. Alternatively, they can choose to view the website with the Smart App Banner instead of launching the App Clip. Both Safari and an [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) remember the person’s decision and won’t display the App Clip card when they visit the site again.

> 💡 **Tip**:  Displaying an App Clip card in Safari on devices that run iOS 15 or later increases the discoverability of your App Clip and reduces the number of taps required to launch the App Clip. However, obscuring your website’s content with the App Clip card may not be ideal. In this case, creating a dedicated page that displays the App Clip card in Safari and linking to it may be a good option to guide people to launch your App Clip.

##### Add Code to Display the Smart App Banner and the App Clip Card on Your Website

In most cases, the best time to add the Smart App Banner and the App Clip card to your website is while you associate your App Clip with your website. Add both by including the following HTML `meta` tag and replacing all placeholders with the appropriate values:

```xml
<meta name="apple-itunes-app" content="app-id=myAppStoreID, app-clip-bundle-id=appClipBundleID, app-clip-display=card">
```

Note how the `meta` tag’s `content` attribute includes the `app-clip-bundle-id`, `app-id`, and `app-clip-display` parameters. By including the `app-id` parameter, you enable the Smart App Banner to open the full app on devices that run iOS 13 or earlier and on devices where Screen Time or a mobile device management (MDM) profile don’t allow App Clips. By including the `app-clip-display` parameter, you display the App Clip card in Safari or an [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) on devices running iOS 15 or later.

> 💡 **Tip**:  If you already display a Smart App Banner on your site, add the `app-clip-bundle-id=appClipBundleID` attribute to the existing `meta` tag for the Smart App Banner, and use the bundle identifier of your App Clip for its value. To display the App Clip card on devices running iOS 15 or later, also add the `app-clip-display` parameter.

Note that the value of a Smart App Banner’s `app-argument` attribute isn’t available to App Clips.

##### Support Invocations From Links People Share in Messages

When you add the `meta` tag to your webpage to support invocations from Safari or an [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController), you automatically add support for invocations from links people share with others in the Messages app. When a person shares a link to the website that displays the banner or App Clip card, the recipient can tap the link to instantly launch your App Clip.

> 💡 **Tip**: If people share the default App Clip URL or the App Clip demo URL in Messages, Messages displays the App Clip card.

Sharing your App Clip in Messages requires that the recipient’s device:

- Runs iOS 14 or later
- Contains the sender as a contact in the Contacts app

If a person shares the link with someone else as an SMS, the recipient must opt to load the rich link before they can tap the preview to launch the App Clip.

> **Note**:  When a person taps a link to a website that displays the Smart App Banner in the Messages app, the invocation URL of your App Clip opens in the default browser.

In addition to the above requirements, you must provide the preview image that appears in the Messages app. To provide the preview image:

1. If your website doesn’t already contain the `property=”og:image”` HTML `meta` tag, add `<meta property=”og:image” content=”https://example.com/example.png”>` to each page that displays the Smart App Banner and the App Clip card.
2. Replace the value of the `content` attribute with the URL of the preview image. Typically, this is the same image you use on the App Clip card. For additional information on displaying link previews in Messages, see [`Best Practices for Link Previews in Messages`](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2444/_index.html).

To enable your App Clip or full app to respond to the invocation from a website that displays the Smart App Banner or the App Clip card in Safari, retrieve the website’s URL upon invocation. Then, use the URL to update the interface of your App Clip to best match the content on the website. For more information on accessing the invocation URL, see [`Responding to invocations`](responding-to-invocations.md).

![A screenshot of a conversation in the Messages app on iPhone that includes a preview of a shared App Clip.](https://docs-assets.developer.apple.com/published/f455903036d0b3eae53cdfd46a6609f3/media-3737844%402x.png)

##### Add the Smart App Banner and App Clip Card to Multiple Websites

In some cases, you may want to add the App Clip card and the Smart App Banner to several websites where each site uses its own domain — for example, if your App Clip serves several individual businesses. However, the default App Clip experience offers only one set of metadata. If you want to display the Smart App Banner on multiple websites where tapping each website’s banner displays a different App Clip card for your App Clip:

1. Add the `meta` tags for the Smart App Banner and App Clip card and for the link previews in the Messages app to each website, for example, `https://example.com`, `https://example2.com`, `https://example3.com`, and so on.
2. Associate each website with your App Clip as described in [`Associating your App Clip with your website`](associating-your-app-clip-with-your-website.md).
3. Configure the default App Clip experience for one website, likely for a more generic landing page. When people launch the App Clip from the landing page, the App Clip could then allow them to choose a business.
4. Create separate advanced App Clip experiences for `https://example2.com`, `https://example3.com`, and so on, as described in [`Configuring App Clip experiences`](configuring-the-launch-experience-of-your-app-clip.md).
5. Use different metadata for each advanced experience you configure; for example, choose custom imagery for the App Clip card.
6. Add code to handle the invocation of your App Clip and to update the interface of your App Clip using the invocation URL — the URL of the website that displays the Smart App Banner or App Clip card. For more information on accessing the invocation URL, see [`Responding to invocations`](responding-to-invocations.md).

> ❗ **Important**:  Remember to associate each domain where you display the App Clip card and the Smart App Banner with your App Clip as described in [`Associating your App Clip with your website`](associating-your-app-clip-with-your-website.md).

To avoid associating your App Clip with multiple domains, consider using one domain and use URLs like `https://example.com/business1` or `https://example.com/business2`. By using one domain, you’ll only have to associate your app and App Clip with `https://example.com` and configure an advanced App Clip experience for each URL.

## See Also

- [Responding to invocations](responding-to-invocations.md)
  Add code to respond to invocations and offer a focused launch experience.
- [Associating your App Clip with your website](associating-your-app-clip-with-your-website.md)
  Enable the system to verify your App Clip to support invocations from your website and devices running iOS 16.3 or earlier.
- [Confirming a person’s physical location](confirming-a-person-s-physical-location.md)
  Add code to quickly confirm a person’s physical location while respecting their privacy.
- [Launching another app’s App Clip from your app](launching-another-app-s-app-clip-from-your-app.md)
  Enable people to launch another app’s App Clip from your app with App Clip links and offer a rich preview of it with the Link Presentation framework.
- [class APActivationPayload](apactivationpayload.md)
  Information that’s passed to an App Clip on launch.
- [NSAppClip](../BundleResources/Information-Property-List/NSAppClip.md)
  A collection of keys that an App Clip uses to get additional capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/supporting-invocations-from-your-website-and-the-messages-app)*