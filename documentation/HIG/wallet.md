---
url: https://developer.apple.com/design/human-interface-guidelines/wallet
framework: HIG
---

# Wallet

**Type:** article

**Platforms:** ios, ipados, macos, visionos, watchos

> **Updated 2026-06-08:** Updated to reflect guidance for iOS 27 and the Pass Designer app.

Wallet helps people securely store their credit and debit cards, driver’s license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.

![A sketch of the Wallet icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/359c72f68cf077a8bb9610e13276f200/technologies-Wallet-intro~dark%402x.png)
People use their cards and passes in Wallet to make Apple Pay purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a concert, or receiving a discount.
When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual’s identity so they can access personal content, and offer detailed receipts and tracking information where it’s most convenient. For developer guidance, see [Wallet](../PassKit/wallet.md).

## Passes
Passes are digital representations of information that people can add to Wallet, like event tickets, boarding passes, membership reward cards, and coupons.
![Three Wallet passes displayed side by side, including a museum membership pass with a dinosaur skull background, a coupon pass for a discount on donuts with a food truck illustration, and a gym pass with a gym equipment background.](https://docs-assets.developer.apple.com/published/d8ddd96fbe8f3a2abc02dd6d8f8942bf/wallet-passes-hero%402x.png)
**Offer to add new passes to Wallet.** When an action results in a new pass, like purchasing an event ticket or registering for a store reward program, you can present system UI that adds the pass to Wallet with one tap. For frequent, predictable actions like checking in for a flight, you can add passes in the background after a person grants a one-time authorization, so they don’t need to tap an Add to Apple Wallet button each time. Wallet notifies the person whenever a pass is added. If someone wants to review a pass first, you can show a custom view with an Add to Apple Wallet button. For developer guidance, see [addPasses(_:withCompletionHandler:)](../PassKit/PKPassLibrary/addPasses(_:withCompletionHandler:).md), [PKPassLibrary.Capability.backgroundAddPasses](../PassKit/PKPassLibrary/Capability/backgroundAddPasses.md), and [PKAddPassesViewController](../PassKit/PKAddPassesViewController.md).
**Help people add a pass created outside your app.** If someone creates a pass using your website or another device, suggest adding it to Wallet the next time they open your app. If people decline your suggestion, don’t ask them again.
**Add related passes as a group.** If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at once so people don’t have to add each one individually. If your website distributes a group of passes, such as a set of event tickets, bundle them together so people can download them all at once. For developer guidance, see [Distributing and updating a pass](../WalletPasses/distributing-and-updating-a-pass.md).
**Display an Add to Apple Wallet button to let people add an existing pass not already in Wallet.** If someone previously declined your suggestion to add a pass to Wallet — or if they removed the pass — a button makes it easy to add the pass if they change their mind. You can display an Add to Apple Wallet button wherever corresponding pass information appears in your app. For developer guidance, see [PKAddPassButton](../PassKit/PKAddPassButton.md). An Add to Apple Wallet badge is also available for emails and webpages; for guidance, see [Add to Apple Wallet guidelines](https://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).
![A screenshot of a food truck app on iPhone displaying a coupon pass offering 20% off a dozen donuts, with an Add to Apple Wallet button below the pass.](https://docs-assets.developer.apple.com/published/c34159672db99555d7312e0c2491d96a/wallet-passes-add-to-apple-wallet%402x.png)
**Let people jump from your app to their pass in Wallet.** Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly. Label the link something like “View in Wallet.”
**Tell the system when your passes expire.** Wallet automatically hides expired passes to reduce crowding, and provides a button that lets people revisit them. To help ensure the system hides passes appropriately, set the expiration date, relevant date, and voided properties of each pass correctly; for developer guidance, see [Pass](../WalletPasses/Pass.md).
**Always get permission before deleting passes from Wallet.** For example, you could include an in-app setting that lets people specify whether they want to delete passes manually or allow automatic removal. If necessary, you can show an alert before deleting a pass.
**Help the system suggest a pass when relevant.** Ideally, passes automatically appear when they’re needed so people don’t have to manually locate them. When you provide information about when and where your pass is relevant, the system can display a link to it on the Lock Screen when people are most likely to want it. For example, a gym membership card could appear on the Lock Screen as people enter the gym. For certain types of passes, like event tickets, the system can also start a Live Activity. For developer guidance, see [Showing a Pass on the Lock Screen](../WalletPasses/showing-a-pass-on-the-lock-screen.md).
![A screenshot of the bottom portion of the Lock Screen on iPhone showing a banner from the Gym app that reads 'Get ready for today's workout! Open your membership pass to badge in.'](https://docs-assets.developer.apple.com/published/34b7be1dc0d51e64da8d5e5f0e983c23/wallet-passes-pass-notification~dark%402x.png)
![A screenshot of the bottom portion of the Lock Screen on iPhone showing a Live Activity for a soccer event ticket, displaying the seat location at level 3, row 12, seat 5.](https://docs-assets.developer.apple.com/published/4f79850739af90cf3131a2a4d2d258c7/wallet-passes-pass-live-activity~dark%402x.png)
**Keep passes up to date.** Physical passes don’t typically change, but a digital pass can reflect changes as they happen. An airline boarding pass, for example, can automatically update to display flight delays and gate changes.
**Use change messages only for updates to time-critical information.** A change message interrupts people, so send one only for updates they need to know about. For example, people need to know when there’s a gate change for a flight, but they don’t need to know when a customer service phone number changes. Never use a change message for marketing or other noncritical communication. Change messages are available per-field; for developer guidance, see [Adding a Web Service to Update Passes](../WalletPasses/adding-a-web-service-to-update-passes.md).

## Pass anatomy
You define the content and structure of a pass using a combination of pass fields and semantic tags. Pass fields define what information appears on a pass and how it’s arranged. Semantic tags describe pass content to the system, enabling features like surfacing a pass when it’s needed, and featured actions, which are quick links to related content like venue directions or event guides. For poster event and semantic boarding passes, semantic tags are required and enable automatic layout. Include pass fields alongside semantic tags for these pass types too, so the passes display correctly on devices running older versions of iOS.
In some cases, you can provide supplemental information that people can access via sheets linked from the front of the pass. The back of the pass holds settings and information people rarely need to access, like legal text.
For developer guidance, see [Wallet Passes](../WalletPasses.md).

### Pass field types
Pass fields are organized into the following areas:
- Logo and logo text fields: Show the brand icon and name; they remain visible when the pass is collapsed in Wallet.
- Header fields: Show critical information that remains visible when the pass is collapsed.
- Primary field: Shows the most important information people need.
- Secondary and auxiliary fields: Show useful, but less critical information.
- Footer fields: Show supplemental information, such as pass category (for example, “Family” or “Annual”).
- Back fields: Show supplemental details that appear in pass details in Wallet.
Layout varies by pass style. For developer guidance, see [Defining the metadata of your Wallet Pass](../WalletPasses/defining-the-metadata-of-your-wallet-pass.md).

## Designing passes
Wallet uses a consistent visual style to build familiarity and trust. Instead of merely replicating the appearance of its physical counterpart, design a clean, simple pass that feels at home in Wallet.
![A screenshot of a museum membership pass open in Wallet on iPhone, showing a full-art background with a dinosaur skull illustration, a QR code, and member details. Below the pass are two featured actions: View Membership Benefits and Go to Location.](https://docs-assets.developer.apple.com/published/3dbde17f0d57e64eadf0fe0a0128ee8e/wallet-passes-wallet-app~dark%402x.png)
Use Pass Designer to design and preview passes for Apple Wallet. Starting from Apple-provided templates or a blank pass, you can create boarding passes, coupons, event tickets, store cards, generic passes, and poster generic passes. For more information, see [Creating a pass with Pass Designer](../WalletPasses/creating-a-pass-with-pass-designer.md).
![A screenshot of Pass Designer on Mac showing a preview of a museum poster generic pass with an illustration featuring a dinosaur skull, butterflies, and marine creatures, along with member details and a QR code.](https://docs-assets.developer.apple.com/published/79bbd59850b42bee6f496e9483663eda/wallet-pass-pass-designer-overview~dark%402x.png)
**Design a pass that looks great and works well on all devices.** Passes can look different depending on the device. For example, a pass on Apple Watch shows less information and fewer images than on iPhone. Don’t put essential information in elements that might be unavailable on certain devices, and avoid adding padding to images; for example, watchOS crops white space from some images. For guidance, see [watchOS](wallet.md#watchOS).
**Keep the pass front uncluttered.** Show essential information, like an event date or account balance, in the header so people can see it when the pass is collapsed in Wallet. Use the rest of the pass front for information people need quick access to. Place details people don’t need often on the additional pass information sheet.
**Make your pass instantly identifiable.** Use brand colors and visual elements like images, icons, and full-art backgrounds to help people recognize your pass at a glance.
**Ensure sufficient contrast between background and text colors.** Pick label colors that keep text legible against both solid backgrounds and background images.
![A gym membership pass with a solid purple background and white label text that's clearly legible against the background.](https://docs-assets.developer.apple.com/published/1ea332e76886bcf95c9514008b8c9e4b/wallet-passes-text-sufficient-contrast%402x.png)
![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)
![A gym membership pass with a solid purple background and label text that's difficult to distinguish from the background.](https://docs-assets.developer.apple.com/published/9b0f80a6e76155b529ef1351dbf58977/wallet-passes-text-insufficient-contrast%402x.png)
![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)
![A concert ticket pass with an image background and white label text that's clearly legible against the background.](https://docs-assets.developer.apple.com/published/6415f7fb142ae3c942e446a23d66b0b3/wallet-passes-background-sufficient-contrast%402x.png)
![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)
![A concert ticket pass with an image background and label text that's difficult to distinguish from the background.](https://docs-assets.developer.apple.com/published/bd8077b53db433cfb9c95cd0d42327ab/wallet-passes-background-insufficient-contrast%402x.png)
![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)
**Use language that works on any device.** Passes can appear on multiple devices, so use text that makes sense everywhere. For example, “Slide to view” is meaningful on iPhone but doesn’t apply on Apple Watch.

## Pass styles
You can choose from a variety of pass styles. Each one defines the appearance and layout of your pass.

### Boarding passes
The boarding pass style is for travel tickets: airline boarding passes, train tickets, bus tickets, boat tickets, and generic transit passes. Typically, each pass corresponds to a single trip with a specific starting and ending point. Use semantic tags for airline boarding passes; use pass fields for all other transit types. For developer guidance, see [Creating an airline boarding pass using semantic tags](../WalletPasses/creating-an-airline-boarding-pass-using-semantic-tags.md).
![An airline boarding pass on a blue background for a flight from San Francisco (SFO) to Tokyo (NRT), displaying passenger details, boarding information, and a QR code.](https://docs-assets.developer.apple.com/published/0c4e6d08916a6742a5966d4407222316/wallet-passes-types-airline-boarding%402x.png)

### Coupons
The coupon style is for coupons, special offers, and other discounts. For developer guidance, see [Creating a coupon pass](../WalletPasses/creating-a-coupon-pass.md).
![A food truck coupon pass with a strip image of a food truck across the upper portion and a solid blue background below, offering 20% off a dozen donuts, with member details and a barcode at the bottom.](https://docs-assets.developer.apple.com/published/a6e91e486376e34259a262cab1863ab1/wallet-passes-types-coupon%402x.png)

### Event tickets
The event ticket pass style is for entry into events like sporting events, concerts, movies, and plays. Typically each pass corresponds to a specific event, but you can also use a single pass for multiple events, as with a season ticket. An event ticket supports a full-art background to evoke the look and feel of your event. For developer guidance, see [Creating a poster event pass using semantic tags](../WalletPasses/creating-an-event-pass-using-semantic-tags.md).
![A soccer event poster ticket with an illustration of a soccer player kicking a ball in a stadium, displaying match details, seat information, and a barcode.](https://docs-assets.developer.apple.com/published/e8fa49aaf4a7e6b3e29c0ed080799ec1/wallet-passes-types-poster-event-ticket%402x.png)
Non-poster style event tickets use standard pass fields and can use a background image and thumbnail.
![A soccer event ticket with a blurred full-image background of a soccer player in motion, displaying event details, seat information, and a barcode at the bottom.](https://docs-assets.developer.apple.com/published/6bf21fa9739d07f58dcf311d48303036/wallet-passes-types-event-ticket-background%402x.png)
![A soccer event ticket on a solid dark blue background, displaying event details, seat information, a thumbnail, and a barcode at the bottom.](https://docs-assets.developer.apple.com/published/ec1d8c8c37a4b262cc1deab5e614581b/wallet-passes-types-event-ticket%402x.png)

### Store cards
The store card style is for store loyalty cards, discount cards, points cards, and gift cards. If an account carries a balance, the pass usually displays it. For developer guidance, see [Creating a store card pass](../WalletPasses/creating-a-store-card-pass.md).
![A coffee shop store card with a strip illustration of a coffee shop scene and a solid dark red background, displaying member name, points balance, reward value, and a QR code.](https://docs-assets.developer.apple.com/published/8c9f0d6bc420749481a3cf4d4091a48a/wallet-passes-types-store-card%402x.png)

### Poster generic passes
The poster generic pass style features a full background image and a pass field layout distinct from other pass styles, offering a flexible option that supports a wide range of use cases. It’s not tied to a specific category, so you can use it whenever another pass style doesn’t fit.
![A museum poster generic pass with a full-art illustration featuring a dinosaur skull, butterflies, and marine creatures, displaying member details and a QR code.](https://docs-assets.developer.apple.com/published/b36adaf362945cdf359aeb21e7e01ead/wallet-passes-types-generic-poster-pass%402x.png)

### Generic passes
The generic style is for passes that don’t fit the other categories, such as a gym membership card or coat-check claim ticket. For developer guidance, see [Creating a generic pass](../WalletPasses/creating-a-generic-pass.md).
![A gym membership generic pass on a solid purple background with a dumbbell thumbnail, member details, and a barcode at the bottom.](https://docs-assets.developer.apple.com/published/1ea332e76886bcf95c9514008b8c9e4b/wallet-passes-types-generic-pass%402x.png)

## Pass images
Passes support a variety of image types. Create pass images in PNG format in @2x and @3x format.
**Reserve pass images for visual content.** Embedded text isn’t accessible and may not be visible if images don’t display on all devices. For text information, use text fields and semantic tags instead. Use Pass Designer or corresponding APIs to add barcodes rather than embedding them in pass images.
**Keep image file sizes small.** People can receive passes via email or a webpage. To make downloads as fast as possible, use the smallest image files that still look great.
**Provide a pass icon.** The system uses it to represent your pass on the Lock Screen, in Mail, and on passes in Wallet. You can use your app icon or design a separate one.

### Logo
The logo appears in the top leading corner of passes with pass fields. It’s typically a horizontal text logo representing your brand, optionally combined with a graphic element.
![The top portion of a food truck coupon pass with a callout identifying the logo position in the top-left corner of the pass.](https://docs-assets.developer.apple.com/published/84f4b3c76352c6892cdf1790ae1a28a6/wallet-passes-images-logo~dark%402x.png)
|  |  |
| --- | --- |
| **Supported pass styles** | Non-semantic airline boarding passes, non-airline boarding pass styles, coupons, non-poster event tickets, generic passes, store cards |
| **Filename** | logo.png |
| **Minimum width** | 50 pt |
| **Maximum width** | 160 pt |
| **Height** | 50 pt |

**Avoid inner drop shadows on logo artwork.** They can reduce legibility when the logo renders on the pass.
![A brown paper bag icon with a flat appearance and no inner drop shadow.](https://docs-assets.developer.apple.com/published/5bc53b33abd72ad21cac57c52a4e848c/wallet-passes-images-logo-no-shadow%402x.png)
![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)
![A brown paper bag icon with an inner drop shadow applied, creating a recessed effect inside the icon shape.](https://docs-assets.developer.apple.com/published/3ecc13739f3f900734971cf1527d11fe/wallet-passes-images-logo-with-shadow-incorrect%402x.png)
![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

### Primary logo
Like the logo, the primary logo appears in the top-leading corner of your pass, but is used exclusively for semantic passes.
![The top portion of an airline boarding pass with callouts identifying a square primary logo in the top-left corner and the logo text beside it.](https://docs-assets.developer.apple.com/published/f66040775fcaf390d9277bb6e1735150/wallet-passes-images-primary-logo-square~dark%402x.png)
![The top portion of an airline boarding pass with a callout identifying a rectangular text-based primary logo in the top-left corner.](https://docs-assets.developer.apple.com/published/11bc5f9202e4f4de1e19a170fcfdf58c/wallet-passes-images-primary-logo-wide~dark%402x.png)
|  |  |
| --- | --- |
| **Supported pass styles** | Airline boarding passes, poster event tickets, and poster generic passes |
| **Filename** | primaryLogo.png |
| **Minimum width** | 30 pt |
| **Maximum width** | 126 pt |
| **Height** | 30 pt |


### Secondary logo
The secondary logo displays an additional logo for a ticket issuer or event organizer. It appears in the bottom-trailing corner of a poster event ticket.
![The bottom portion of a soccer event poster ticket with a callout identifying the secondary logo in the bottom-trailing corner.](https://docs-assets.developer.apple.com/published/4838b2c7111140a26343252d8008437a/wallet-passes-images-secondary-logo~dark%402x.png)
|  |  |
| --- | --- |
| **Supported pass styles** | Poster event ticket |
| **Filename** | secondaryLogo.png |
| **Minimum width** | 12 pt |
| **Maximum width** | 135 pt |
| **Height** | 12 pt |


### Icon
Icons are square and represent your company or brand when your pass appears on the Lock Screen, in Mail, and on passes in Wallet. The system automatically applies rounded corners, so you don’t need to round them.
![A screenshot of the bottom portion of the Lock Screen on iPhone showing an airline boarding pass banner that reads 'Get ready for flight AP 1042 to Tokyo!', with the pass icon appearing in the leading edge of the banner.](https://docs-assets.developer.apple.com/published/d8a1fffbcdf0f911518fa4fb64699576/wallet-passes-images-icon-notification~dark%402x.png)
![The bottom portion of an airline boarding pass open in Wallet on iPhone, with the pass icon visible in the bottom-leading corner of the pass, and two featured actions below: Go to Terminal I and Track Luggage.](https://docs-assets.developer.apple.com/published/845fcef8d36d807c44258692b62753be/wallet-passes-images-icon-wallet~dark%402x.png)
|  |  |
| --- | --- |
| **Supported pass styles** | All |
| **Filename** | icon.png |
| **Width** | 38 pt |
| **Height** | 38 pt |


### Strip image
Strip images appear on coupons and store cards to reinforce your brand or offer. Because text can appear over strip images, ensure sufficient contrast between your text and the image. Keep areas behind text uncluttered, and place important visual elements toward the bottom or trailing edge. Avoid embedding text in the strip image.
![The upper portion of a food truck coupon pass with callouts identifying the primary field and the strip image, outlined with dashed borders.](https://docs-assets.developer.apple.com/published/59068cbef1eeea077055c4e81cb7b7c7/wallet-passes-images-strip-image~dark%402x.png)
|  |  |
| --- | --- |
| **Supported pass styles** | Coupon, store card |
| **Filename** | strip.png |
| **Width** | 375 pt |
| **Height** | 144 pt |


### Thumbnail
Thumbnails are small images, such as a movie poster, that appear on event tickets and generic passes. Thumbnails are square — use rounded corners on your artwork and export as a transparent PNG.
![The top portion of a gym membership pass on a solid purple background with a callout identifying the thumbnail in the upper-trailing area of the pass.](https://docs-assets.developer.apple.com/published/13a90993f985cfdc92fd1a95001ea026/wallet-passes-images-thumbnail~dark%402x.png)
|  |  |
| --- | --- |
| **Supported pass styles** | Event ticket, generic pass |
| **Filename** | thumbnail.png |
| **Minimum width** | 60 pt |
| **Maximum width** | 90 pt |
| **Height** | 90 pt |


### Background
The background image is the visual centerpiece of a pass.
![A soccer event ticket with a blurred full-image background of a soccer player in motion, displaying event details, seat information, and a barcode at the bottom.](https://docs-assets.developer.apple.com/published/6bf21fa9739d07f58dcf311d48303036/wallet-passes-types-event-ticket-background%402x.png)
![A food truck coupon pass with a background illustration of a food truck in an outdoor setting, a barcode overlaid on the illustration, and coupon details at the top and bottom.](https://docs-assets.developer.apple.com/published/7a7b68c3d3b8b75c41138708a1e2a7f5/wallet-passes-images-background-unblurred%402x.png)
**Non-poster pass backgrounds**
|  |  |
| --- | --- |
| **Supported pass styles** | Event tickets |
| **Filename** | background.png |
| **Width** | 343 pt |
| **Height** | 503 pt |

**Poster pass backgrounds**
|  |  |
| --- | --- |
| **Supported pass styles** | Poster event tickets, poster generic passes |
| **Filename** | artwork.png |
| **Width** | 358 pt |
| **Height** | 448 pt |

Position content within the safe area — on poster generic passes and poster event tickets, a material strip covers the bottom edge of the image. If your pass includes a barcode, account for it in your background design. You can preview your pass layout in Pass Designer to verify placement. For developer guidance, see `footerBackgroundColor` in [Pass](../WalletPasses/Pass.md).
![A museum poster generic pass with a background illustration featuring a dinosaur skull, butterflies, and marine creatures, with a QR code and member details at the bottom.](https://docs-assets.developer.apple.com/published/b36adaf362945cdf359aeb21e7e01ead/wallet-passes-images-background-layout-qr-code%402x.png)
![A museum poster generic pass with a background illustration featuring a dinosaur skull, butterflies, and marine creatures. Blue overlays show the safe areas for pass content, including a header area at the top and QR code and footer areas below.](https://docs-assets.developer.apple.com/published/5dab4daa5f28b378c82d0630aa6d9071/wallet-passes-images-background-layout-qr-code-safe-areas%402x.png)
![An art museum poster generic pass with a full-art background illustration of a waterfall scene, with a barcode and member details at the bottom.](https://docs-assets.developer.apple.com/published/8492f0d3a48b91fe4ee188dd831aeb0c/wallet-passes-images-background-layout-barcode%402x.png)
![A background artwork image of a waterfall scene. Blue overlays show the safe areas for pass content, including a header area at the top and barcode and footer areas below.](https://docs-assets.developer.apple.com/published/693aa10fac97cee7b647e6b85df925b2/wallet-passes-images-background-layout-barcode-safe-areas%402x.png)

### Footer
The footer is only available for airline boarding passes.
|  |  |
| --- | --- |
| **Supported pass styles** | Airline boarding passes |
| **Filename** | footer.png |
| **Width** | 268 pt |
| **Height** | 15 pt |


## Order tracking
When you support order tracking, Wallet can display information about an order a customer placed through your app or website, updating the information whenever the status of the order changes. In iOS 17 and later, you can help people start tracking their order right from your app or website and offer additional ways to add their order to Wallet.
![A screenshot of an order fulfillment screen for a food truck app on iPhone. The screen displays information about an order placed, and includes a status bar, shipping address, list of items ordered, and additional order details.](https://docs-assets.developer.apple.com/published/ed4f2ca19afe5b27b09c7851051fd2c5/wallet-ot-status-order-placed~dark%402x.png)
![A screenshot of an order fulfillment screen for a food truck app on iPhone. The screen displays information about an order placed, and denotes that the order was delivered today. The screen includes the shipping address, a link to track the shipment, a list of items ordered, and additional order details.](https://docs-assets.developer.apple.com/published/a91c2c9ade272d22b0a3ba37eb48599c/wallet-ot-status-delivered~dark%402x.png)
Wallet presents a dashboard that displays a customer’s active and completed orders. People can choose an order to view details about it, like the items they ordered and fulfillment information for shipping and pickup.
![A screenshot of a dashboard that displays an order history screen for a food truck app on iPhone. The screen displays a search field, a list of active orders, and a list of orders placed this month.](https://docs-assets.developer.apple.com/published/0a8edf108ad24a35060a65ff3cd0fdd6/wallet-ot-dashboard~dark%402x.png)
The [Wallet Orders](../WalletOrders.md) schema defines the properties you use to provide order data like product descriptions, order status, contact information, and shipping and pickup details, including estimated arrival dates, addresses, tracking numbers, and pickup instructions. Wallet displays the information you supply within consistent, system-defined interfaces. To help people get the information they need quickly and conveniently, supply as much information as you can, using the properties that match your order processes.
![A screenshot of an order fulfillment screen for a food truck app on iPhone. The screen displays information about an order placed, and includes a status bar, shipping address, list of items ordered, and additional order details. Callouts identify different fields on the screen, including the merchant logo and display name, the order status and description, the tracking link, and various line items.](https://docs-assets.developer.apple.com/published/0c16bbc53c5ba163fbd09896daaca6d3/wallet-ot-status-on-the-way-fields~dark%402x.png)
**Make it easy for people to add an order to Wallet.** For example, when a customer completes an Apple Pay transaction in your app or website, use [PKPaymentOrderDetails](../PassKit/PKPaymentOrderDetails.md) (app) or [ApplePayPaymentOrderDetails](../ApplePayontheWeb/ApplePayPaymentOrderDetails.md) (web) to automatically add the order to Wallet. In iOS 17 and later, you can use [AddOrderToWalletButton](../FinanceKitUI/AddOrderToWalletButton.md) to display the system-provided Track with Apple Wallet button in relevant areas of your app or website — such as in pages for order confirmation, status, or tracking — or in emails to customers. If a person already added an order to Wallet, trying to add it again opens Wallet and displays the order.
**Make information about an order available immediately after people place it.** People need to confirm that their order was received, even when payment, processing, and fulfillment are still pending. If you won’t have details until a later time, provide the data you have at the time of the order and supply a status [description](https://developer.apple.com/documentation/walletorders/order) like “Check back later for full order details.”
**Provide fulfillment information as soon as it’s available, and keep the status up to date.** When you supply fulfillment data or you change the status of an order, the system updates the order information and can automatically send a notification to customers. The system uses the fulfillment status you report to update the order’s current status to a value like Order Placed, Processing, Ready for Pickup, Picked Up, Out for Delivery, Delivered, or — if something goes wrong — Issue or Canceled. For guidance on describing a status, see [Displaying order and fulfillment details](wallet.md#Displaying-order-and-fulfillment-details).
**Supply a high-resolution logo image that uses a nontransparent background.** The system displays your logo image in the dashboard and detail view, so you want to make sure that people can instantly recognize it at various sizes. Use the PNG or JPEG format to create a logo image that measures 300x300 pixels. To help ensure that your logo image renders correctly, be sure to use a nontransparent background. For developer guidance, see [logo](https://developer.apple.com/documentation/walletorders/merchant).
**Supply distinct, high-resolution product images that use nontransparent backgrounds.** The system displays a product’s image — along with descriptive information you supply — in the detail views, order dashboard, and notifications for an order or a fulfillment. When creating a product image, use a straightforward depiction and a solid, nontransparent background. Showing a product in a “lifestyle” context or against a busy background can make the item hard to distinguish at small sizes. For each product, use the PNG or JPEG format to create an image that measures 300x300 pixels.
![An illustration of a donut, representing a product image. Horizontal and vertical lines extend along the bottom and right side of the image, and include labels that denote the illustration is 300 pixels wide by 300 pixels high.](https://docs-assets.developer.apple.com/published/60f1baa1a1e6d5c9532421a66ee7a4da/wallet-ot-product-images~dark%402x.png)
**In general, keep text brief.** People appreciate being able to read text at a glance, and the system can truncate text that’s too long.
**Use clear, approachable language, and localize the text you provide.** You want to make sure that all your customers can read the information in an order. Also, make sure the price you show matches the final price the customer confirmed.

### Displaying order and fulfillment details
An order gives people ways to contact the merchant and displays details about their Apple Pay purchase, including fulfillment status and per-item information.
**Provide a link to an area where people manage their order.** When you provide a universal link, people can open your order management area even if they don’t have your app installed. To learn more about universal links, see [Allowing apps and websites to link to your content](../Xcode/allowing-apps-and-websites-to-link-to-your-content.md); for developer guidance, see [Order](../WalletOrders/Order.md).
**Clearly describe each item so people can verify that their order contains everything they expect.** You can use the [LineItem](../WalletOrders/LineItem.md) property to provide information like a product’s price, name, and image. An order lists the line items for every item the customer ordered; a fulfillment lists only the line items that fulfillment includes. When appropriate, you can also attach a PDF receipt to an individual transaction related to an order.
**Supply a prioritized list of your apps that might be installed on the device.** The system uses this list when it needs to display a link to your app within the order details view. For example, if you provide multiple apps and more than one of them is installed on the device, the system displays a link to the installed app that’s highest on your list. If none of your apps are installed on the device, the system displays a link to the first app on your list. For developer guidance, see [Order](../WalletOrders/Order.md).
**Avoid sending duplicate notifications.** For example, you can tell the system to avoid sending order-related notifications through Wallet when the customer has one of your associated apps installed.
**Make it easy for customers to contact the merchant.** Provide multiple contact methods, so people can choose the one that works best for them. At minimum, you need to provide a link to the merchant’s website or landing page, but you can also provide a Messages for Business link, a phone number, an email address, and a link to a support page. When people choose the Contact button in an order, the system displays a menu of the contact methods you supply. For developer guidance, see [Merchant](../WalletOrders/Merchant.md).
![A screenshot of an order detail screen for a food truck app on iPhone. The screen displays a list of donuts ordered. Above the list is an overlay containing buttons to message or email the merchant, get online support, or call customer service.](https://docs-assets.developer.apple.com/published/6024778951ce712247405d2668a4043d/wallet-ot-contacts~dark%402x.png)
**Help people track their order.** A multi-item order can have multiple fulfillments, where each fulfillment is either shipping or pickup. For example, if a customer orders a pair of shoes and a T-shirt, the customer might want to have one item shipped, while picking up the other. Regardless of fulfillment type, you need to supply enough information for people to know where their items are and when to expect them at the destination they specified. In addition to an estimated time of arrival, here’s some information that people particularly appreciate:
- A link that opens the carrier’s website to a page with information about a shipping fulfillment. When possible, provide a direct link — in addition to a tracking number — so people can easily view the most up-to-date shipping information. If necessary, display this link on any intermediate order-tracking page you open.
- A scannable barcode when one is required to pick up the order in a pickup fulfillment. It’s convenient when people can offer the barcode from within Wallet instead of finding it in an email or webpage.
- Clear, detailed instructions that can help people receive or pick up their order.
![A screenshot of an order fulfillment screen for a food truck app on iPhone. The top of the screen displays information about an order placed, and denotes that the order arrives tomorrow. The screen includes the shipping address, a link to track the shipment, a list of items ordered, and additional order details. The bottom of the screen displays another order placed, which is ready for pickup. In place of the shipping address is a Barcode button and a pickup address.](https://docs-assets.developer.apple.com/published/aff7dc7c05433774a26d760ce124eb83/wallet-ot-status-pickup-details~dark%402x.png)
**Keep the fulfillment screen centered on order tracking.** For example, if you recommend your app or other services to customers, be sure to prioritize order-tracking information over other content in the screen.
**Choose shipping-fulfillment values that match the details you have about the shipping process.** If you know the carrier, enter its name in the `carrier` property; otherwise, leave the default “Track Shipment” value. If you can access details about a carrier’s interim shipping steps — such as when a fulfillment is on the way or out for delivery — indicate each step by using specific status values like `onTheWay`, `outForDelivery`, or `delivered`. In contrast, if you don’t have access to a carrier’s shipping details, use the `shipped` status. In both cases, provide a tracking link (when one is available) so people can track their order on their own. For developer guidance, see [ShippingFulfillment](../WalletOrders/ShippingFulfillment.md).
**Keep customers informed through relevant fulfillment status descriptions.** A great status message is approachable, accurate, and clearly related to the status it describes. In addition to supplying information that helps people understand the status of their order, a status message also gives you an opportunity to use your brand’s communication style.
**Be direct and thorough when describing an Issue or Canceled status.** People generally need to know why there’s a problem and what they can do about it.

## Identity verification
On iPhone running iOS 16 and later, people can store an ID card in Wallet, and later allow an app or App Clip to access information on the card to verify their identity without leaving their current context. For example, a person might need to confirm their identity when they apply for a credit card within their banking app. To learn how to support in-person mobile ID verification, see [ID Verifier](id-verifier.md).

> **Note:** Apple doesn’t create or see the ID documents that people add to Wallet, and when people agree to share identifying information with your app, you receive only encrypted data that isn’t readable on the device. For developer guidance, see [Requesting identity data from a Wallet pass](../PassKit/requesting-identity-data-from-a-wallet-pass.md).
To help you offer a consistent experience that people can trust, Apple provides a Verify with Wallet button you can use in your app when you need to ask for identity verification. The button reveals a sheet that describes your request and lets people agree to share their information or cancel.
**Present a Wallet verification option only when the device supports it.** If the current device can’t return the identity information you request, don’t display a Verify with Apple Wallet button. Be prepared to present a fallback view that offers a different verification method if Verify with Apple Wallet isn’t available; for developer guidance, see [VerifyIdentityWithWalletButton](../PassKit/VerifyIdentityWithWalletButton.md).
**Ask for identity information only at the precise moment you need it.** People can be suspicious of a request for personal information if it doesn’t seem to be related to their current action. If your app needs identity verification, for example, wait to ask for this information until people are completing the process or transaction that requires it; don’t request verification before people are ready to start the process or when they’re simply creating an account.
**Clearly and succinctly describe the reason you need the information you’re requesting.** You must write text that explains why people need to share identity information with your app (this text is called a *purpose string* or *usage description string*). The system displays your purpose string in the verification sheet so people can make an informed decision. Here are a couple of examples:
| To verify… | To support… | Example purpose string |
| --- | --- | --- |
| Identity | Opening an account for which proof of identity is legally required to prevent fraud | Federal law requires this information to verify your identity and also to help [App Name] prevent fraud. |
| Driving privilege | Renting a vehicle that requires legal driving privileges | Applicable state law requires [App Name] to verify your driving privileges. |

For each purpose string, aim for a brief, complete sentence that’s direct, specific, and easy for everyone to understand. Use sentence case, avoid passive voice, and include a period at the end.
**Ask only for the data you actually need.** People may lose trust in your app if you ask for more data than you need to complete the current task or action. For example, if you need to ensure that a customer is at least a certain age, use a request that specifies an age threshold; avoid requesting the customer’s current age or birth date. For developer guidance, see [age(atLeast:)](../PassKit/PKIdentityElement/age(atLeast:).md).
**Clearly indicate whether you will keep the data and — if you need to keep it — specify how long you’ll do so.** To help people trust your app, it’s essential to explain how long you might need to keep the personal information they agree to share with you. When you use PassKit APIs to specify a duration — such as a particular period, indefinitely, or only as long as it takes to complete the current verification — the system automatically displays explanatory content in the verification sheet. For developer guidance, see [PKIdentityIntentToStore](../PassKit/PKIdentityIntentToStore.md).
**Choose the system-provided verification button that matches your use case and the visual design of your app.** The system provides the following button labels to support various use cases:
| Button type | Consider using when… |
| --- | --- |
| ![An illustration of a Verify Age with Apple Wallet button.](https://docs-assets.developer.apple.com/published/a85ccec0e59306e1bf8b8d6d6e8107b2/wallet-button-verify-age~dark%402x.png) | Your app can complete the current transaction after you verify a person’s age. An example transaction is making a car available to lease. |
| ![An illustration of a Verify Identity with Apple Wallet button.](https://docs-assets.developer.apple.com/published/28b605e242c790a9cc651292e65687d1/wallet-button-verify-identity~dark%402x.png) | Your app can complete the current transaction after you verify a person’s identity. An example transaction is a car rental. |
| ![An illustration of a Continue with Apple Wallet button.](https://docs-assets.developer.apple.com/published/7b81d85a9aa6446bb2a1f6f222c2d2b9/wallet-button-continue-with~dark%402x.png) | Verify with Wallet forms one part of a verification process that also requires people to supply additional information not provided by Verify with Wallet, such as a Social Security number or phone number. Examples include opening a financial account or performing a background check. |
| ![An illustration of a Verify with Apple Wallet button.](https://docs-assets.developer.apple.com/published/24bda3f866a1c847c6e5eb05eac43a3b/wallet-button-verify-with~dark%402x.png) | Your app can complete the current verification flow without additional steps, but the “Verify Age,” “Verify Identity,” and “Continue” button labels aren’t appropriate for your use case. An example is an app that helps people sign up for a government service. |

All button labels are also available in a multiline variant that the system automatically uses when horizontal space is constrained. For developer guidance, see [PKIdentityButton.Label](../PassKit/PKIdentityButton/Label.md).
The verification button always uses white letters on a black background. You can choose the style that includes a light outline if you need to ensure that the button contrasts well with a dark background in your app. In addition, you can use the [cornerRadius](../PassKit/PKIdentityButton/cornerRadius.md) property to adjust the verification button’s corners to match other related buttons in your interface. For developer guidance, see [PKIdentityButton.Style.blackOutline](../PassKit/PKIdentityButton/Style/blackOutline.md).

## Platform considerations
*No additional considerations for iOS, iPadOS, macOS, or visionOS. Not supported in tvOS.*

### watchOS
On Apple Watch, Wallet displays passes in a scrolling carousel of cards. People can add your pass to their Apple Watch even if you don’t create a watch-specific app, so it’s important to understand how your pass can look on the device.
![A screenshot of a selected flight pass in a list of passes on Apple Watch. The pass includes information about a flight from SFO to LGA. The next pass in the list is a gym membership card with a barcode.](https://docs-assets.developer.apple.com/published/9b54ebf2a350a1e748a38c0b2cc3b74a/watch-card-and-details%402x.png)
People can tap a pass on their Apple Watch to reveal a details screen that displays additional information in a scroll view. In some cases, people can also tap a specific transaction to get more information.
![A screenshot of a flight pass on Apple Watch. The pass includes information about a flight from SFO to LGA, and appears above a QR code.](https://docs-assets.developer.apple.com/published/0f74b7b757684a79981367adf14d6adb/watch-pass-design-intro%402x.png)
Each pass style specifies the fields and images that can appear in the basic layout areas shown below:
![A diagram that shows the basic layout of a pass on Apple Watch. A top row contains a logo image and an essential field area. A second row contains a primary field area. A third row contains a secondary and auxiliary fields area.](https://docs-assets.developer.apple.com/published/717668c6f264c021ef97013edbba4f51/watch-layout-diagram~dark%402x.png)
If some information doesn’t fit within the layout areas, the system displays it in the scrolling details screen.

> **Important:** In every style, watchOS crops the strip image to fit the aspect ratio of the card interface and may crop white space from other images.

## Resources

#### Related
[Apple Pay](apple-pay.md)
[ID Verifier](id-verifier.md)

#### Developer documentation
[FinanceKitUI](../FinanceKitUI.md)
[FinanceKit](../FinanceKit.md)
[PassKit (Apple Pay and Wallet)](../PassKit.md)
[Wallet Passes](../WalletPasses.md)
[Wallet Orders](../WalletOrders.md)

#### Videos
- [What’s new in Wallet](https://developer.apple.com/videos/play/wwdc2026/209) - Explore the newest design updates and developer tools for Apple Wallet passes. Refresh your passes with beautiful new styles for rich, vibrant designs. Discover new barcode formats and a flexible pass actions API. Meet Pass Designer and Pass Builder, powerful tools that simplify designing, personalizing, and distributing your passes at scale.

## Change log
| Date | Changes |
| --- | --- |
| June 8, 2026 | Updated to reflect guidance for iOS 27 and the Pass Designer app. |
| January 17, 2025 | Added specifications for pass image dimensions. |
| December 18, 2024 | Added guidance for the poster event ticket style. |
| September 12, 2023 | Added guidance for helping people add orders to Wallet. |
| February 20, 2023 | Enhanced guidance for presenting order-tracking information and added artwork. |
| November 30, 2022 | Added guidance to include a carrier name in status information for a shipping fulfillment. |
| September 14, 2022 | Added guidelines for using Verify with Wallet, updated guidance on providing shipping status values and descriptions, and consolidated guidance into one page. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/wallet](https://developer.apple.com/design/human-interface-guidelines/wallet)*
