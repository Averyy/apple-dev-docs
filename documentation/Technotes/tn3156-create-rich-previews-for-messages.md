# TN3156: Create rich previews for Messages

**Framework**: Technotes

Learn best practices for creating rich text and image previews for display in the Messages app.

#### Overview

The Messages app on iOS and macOS by default shows inline previews for links as gray bubbles with the page title, domain, and small icon belonging to the linked web page:

![Example Domain](https://docs-assets.developer.apple.com/published/57a6a5d89a59325b0cecb96289d8a822/tn3156_examplecom%402x.png)

You can display images and meaningful captions in these link previews by adding [`Open Graph`](https://developer.apple.comhttps://ogp.me) metadata on your website pages. Here’s an example link preview for `https://www.apple.com/iphone`, which includes an image and title:

![IPhone Photo](https://docs-assets.developer.apple.com/published/9d1f113fb82a880d1f82b444a3b79e2a/tn3156_iphoneapplecom%402x.png)

This appearance results from the following `meta` tags on the webpage:

```html
<meta property="og:title" content="iPhone" />
<meta property="og:image" content="https://www.apple.com/v/iphone/home/t/images/home/og.png?201610171354" />
```

Read the following sections for tips on how to get rich link previews in Messages.

#### Use Consistent Metadata for All User Agents

Serve the same metadata to both mobile and desktop versions of the page. Clients shouldn’t have to change the `User-Agent` header to receive useful metadata.

#### Add Images to Link Previews

Use the `og:image` property to include an image in your link preview. Preview images are displayed large enough to represent the linked page clearly, including relevant details.

Also provide a high-resolution icon in addition to your image. The link preview will use an  [`apple-touch-icon`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4), a favicon, or an icon specified by `<link rel="...">`. If you do not have a preview image of sufficient size or quality, use an `apple-touch-icon` instead.

Avoid text in preview images. Images may be displayed at varying sizes depending on context and device, potentially making text unreadable. For best results, keep the image graphical and use other metadata tags for text. Text provided via metadata is also accessible for people using [`VoiceOver`](https://developer.apple.comhttps://www.apple.com/accessibility/vision/).

#### Add Videos to Link Previews

If you want to display a video in your preview, use a direct link to your video asset via a `meta` tag, rather than a reference to an embeddable video page. With the direct link, the video loads and displays faster, and it uses the system user interface for playback.

If the link preview encounters an `og:video` or `twitter:player:stream` property that points to a downloadable and playable media asset (for example, an MPEG-4 file), the preview downloads the video and automatically plays it back.

Videos that can be streamed but not downloaded, such as [`HTTP Live Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/) (HLS) streams, require the user to tap to start playback. Videos that require embedding HTML will not play inline.

#### Customize Titles in Link Previews

Use the `og:title` property to specify the title of your link preview. Titles should be short and specific enough to distinguish different pages on the same website. For example, product pages should indicate the product name in the title.

Do not put the site name or other branding in the `og:title`. Doing so often leads to duplication of information between the title and other parts of the rich preview, and is semantically incorrect. Use `og:site_name` for the site name instead.

#### Ensure Your Metadata Is Reachable

Link previews do not follow `meta` redirects, nor run JavaScript; metadata must be available directly on the linked page. Server-side redirects are followed, however, and are a good alternative.

Pages that require authentication should still have meaningful metadata, without revealing any sensitive content. For pages that require authentication, the main resource should provide metadata for the page to which access is being provided, and not for the authentication page itself. This avoids showing “Sign In” as the title for every page behind an authentication wall.

#### Respect Resource Usage Guidelines

- Icons should be square, at least 108 pixels per side.
- Images should be at least 900 pixels in width.
- Images less than 150 pixels in width may be ignored or presented as icons.
- The main resource located at the previewed link is limited to 1 MB. The total size of associated resources (icons, images, and videos, etc) is limited to 10 MB.

These recommendations are guidelines only. Limits may change in the future.

#### Enable Social Network Link Previews

For preview links to user posts on social network services, specify the text of the user post via the `og:description` property. In addition:

- The page must be configured with a `twitter:card` value of `summary` or `summary_large_image` as described in the [`X for Websites`](https://developer.apple.comhttps://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary) documentation.
- The page must have a `link` element with a `type` attribute of `application/activity+json` as described in the [`ActivityPub protocol`](https://developer.apple.comhttps://www.w3.org/TR/activitypub/) documentation.

#### Revision History

-  Republished as TN3156. Added social network information.
-  First published as TN2444 “Best Practices for Link Previews in Messages”.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3156-create-rich-previews-for-messages)*